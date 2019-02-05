#!/usr/bin/env python3

import PyPDF2
import time
import argparse
from collections import defaultdict









def fill_temp_with_everything_after_answer(temp, data_base, i, y):
    for j in range(y, len(data_base[i])):
        temp.extend(data_base[i][j])
    for j in range(temp.count(" ")):
        temp.remove(" ")
    return temp


def fill_c_with_only_correct_answer(temp):
    last_cell = "".join(temp)
    last_cell = last_cell[last_cell.index(":") + 1 :]
    f = [z for z, g in enumerate(last_cell) if g == "," and z < 12]
    if len(f) == 0:
        last_cell = last_cell[:1]
    if len(f) == 1:
        last_cell = last_cell[:3:2]
    if len(f) == 2:
        last_cell = last_cell[:5:2]
    if len(f) == 3:
        last_cell = last_cell[:7:2]
    if len(f) == 4:
        last_cell = last_cell[:9:2]
    if len(f) == 5:
        last_cell = last_cell[:11:2]
    return last_cell


def fill_temp_data_after_answers(temp_max, i, temp_data, data_base, temp_data_base):
    for z1 in range(temp_max):
        temp_data_base[i].append(data_base[i][z1])
    temp_data_base[i].append(temp_data)
    return temp_data_base


def delete_strings_after_correct_answers(data_base, lines):
    max_range_for_base = count_lines_in_simple_question(lines)
    temp_data_base = [[] for _ in range(max_range_for_base)]
    for i in range(len(data_base)):
        for y in range(len(data_base[i])):
            temp = []
            if "Answ" in data_base[i][y]:  # find answ
                temp = fill_temp_with_everything_after_answer(temp, data_base, i, y)
                temp_data = fill_c_with_only_correct_answer(temp)
                temp_max = y

        temp_data_base = fill_temp_data_after_answers(
            temp_max, i, temp_data, data_base, temp_data_base
        )

    return temp_data_base


def remove_questions_124_and_144(data_base):
    del data_base[143]
    del data_base[123]
    return data_base


def split_simple_question(data_base):
    TEMPORARY_MEMORY = [[] for _ in range(8)]
    temp_sum = 0
    for i in range(len(data_base)):

        flag = 0
        for y in range(len(data_base[i]) - 1):
            if data_base[i][y].startswith("A."):
                flag = 2
            if data_base[i][y].startswith("B."):
                flag = 3
            if data_base[i][y].startswith("C."):
                flag = 4
            if data_base[i][y].startswith("D."):
                flag = 5
            if data_base[i][y].startswith("E."):
                flag = 6
            if data_base[i][y].startswith("F."):
                flag = 7
            TEMPORARY_MEMORY[flag].append(data_base[i][y])
        TEMPORARY_MEMORY[1].append(data_base[i][len(data_base[i]) - 1])

        # checker
        a = len(TEMPORARY_MEMORY[2])
        b = len(TEMPORARY_MEMORY[3])
        c = len(TEMPORARY_MEMORY[4])
        d = len(TEMPORARY_MEMORY[5])
        e = len(TEMPORARY_MEMORY[6])
        f = len(TEMPORARY_MEMORY[7])
        if "B" in TEMPORARY_MEMORY[1][0] and a < 2 and b < 2:
            print("Not ok")
        if "C" in TEMPORARY_MEMORY[1][0] and a < 2 and b < 2 and c < 2:
            print("Not ok")
        if "D" in TEMPORARY_MEMORY[1][0] and a < 2 and b < 2 and c < 2 and d < 2:
            print("Not ok")
        if (
                "E" in TEMPORARY_MEMORY[1][0]
                and a < 2
                and b < 2
                and c < 2
                and d < 2
                and e < 2
        ):
            print("Not ok")
        if (
                "F" in TEMPORARY_MEMORY[1][0]
                and a < 2
                and b < 2
                and c < 2
                and d < 2
                and e < 2
                and f < 2
        ):
            print("Not ok")
        temp_sum = temp_sum + a + b + c + d + e + f

        for _ in range(len(TEMPORARY_MEMORY)):
            del TEMPORARY_MEMORY[_][:]

    print("temp sum=", temp_sum)

def count_lines_in_simple_question(lines):
    count_question = -1
    for line in lines:
        if line.replace(" ", "").startswith("Question"):
            count_question += 1
    return count_question


def remove_beginning_strings_in_question(temp_data_base):
    remove_number = 0
    for i in range(len(temp_data_base)):
        number_question = 1 + i
        for y in range(4):
            if str(number_question) in temp_data_base[i][y]:
                del temp_data_base[i][y]
        for y in range(5):
            if temp_data_base[i][y] == "":
                remove_number += 1
        del temp_data_base[i][: 1 + remove_number]
        add = "Question " + str(number_question)
        temp_data_base[i].insert(0, str(add))
    return temp_data_base


def split_the_base_into_a_single_one(lines):
    max_range_for_base = count_lines_in_simple_question(lines)
    flag = -1
    temp_data_base = [[] for _ in range(max_range_for_base)]
    a = []
    for line in lines:
        if line.replace(" ", "").startswith("Question"):
            temp_data_base[flag].extend(a)
            flag += 1
            del a[:]
        a.append(line)
    temp_data_base = remove_beginning_strings_in_question(temp_data_base)
    return temp_data_base


def import_data_from_file():
    pdf_file = open("123.pdf", "rb")
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    lines = []
    # for page_now in range(45, 65):
    for page_now in range(read_pdf.getNumPages()):
        page_content = read_pdf.getPage(page_now).extractText()
        lines.extend(page_content.splitlines())
    # lines.extend(a for page_now in range(read_pdf.getNumPages()) for a in read_pdf.getPage(page_now).extractText().splitlines())
    return lines


def remove_page_number(lines):
    lines_now = []
    number_page_inside = 1

    for line in lines:
        temp_line = line.replace(" ", "")
        if temp_line == str(number_page_inside):
            number_page_inside += 1
            continue
        else:
            lines_now.append(line)
    return lines_now


def end_of_loop():
    raise StopIteration


def remove_section_page_footer(lines):
    temp_lines = []
    for line in lines:  # lines before Question 1 contains something
        temp_line = line.replace(" ", "")
        if temp_line.startswith("Question"):
            break
        else:
            if temp_line != "":
                temp_lines.append(line)
    # temp_lines= list(end_of_loop() if line.replace(' ', '').startswith('Question') else line for line in lines)
    return delete_page_footer(lines, temp_lines)


def delete_page_footer(lines, temp_lines):
    lines_now = []
    flag = True
    for line in lines:
        for wrong_lines in temp_lines:
            if line.replace(" ", "") == wrong_lines.replace(" ", ""):
                flag = False
        if flag == True:
            lines_now.append(line)
        else:
            flag = True
    return lines_now


def delete_empy_lines_at_beginning_of_the_document(lines):
    while not lines[0].replace(" ", "").startswith("Question"):
        del lines[0]
    return lines


def delete_empy_lines_in_document(lines):
    lines_now = []
    for line in lines:
        if line == "":
            continue
        else:
            lines_now.append(line)
    return lines_now


if __name__ == "__main__":

    start = time.time()
    parser = argparse.ArgumentParser(description="Program for learning from script")
    parser.add_argument("-f", default="123.pdf")
    # , help='Write file name', required=True
    args = parser.parse_args()

    if args.f == "Write file name":
        print("I can tell that no argument was given and I can deal with that here.")
    elif args.f == "123.pdf":
        print("Ok")
    else:
        print("I can not find it")

    lines = import_data_from_file()
    lines = remove_page_number(lines)
    lines = remove_section_page_footer(lines)
    lines = delete_empy_lines_at_beginning_of_the_document(lines)
    lines = delete_empy_lines_in_document(lines)
    data_base = split_the_base_into_a_single_one(lines)
    data_base = delete_strings_after_correct_answers(data_base, lines)
    data_base = remove_questions_124_and_144(data_base)
    split_simple_question(data_base)
    stop = time.time()

    print("The program worked for %.3f seconds" % (stop - start))
