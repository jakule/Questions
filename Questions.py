#!/usr/bin/env python3

import PyPDF2
import time
import argparse
from collections import defaultdict

TEMPORARY_MEMORY = [[] for _ in range(24)]

class Question:
    def __init__(self, contents, correct_answer):
        self.contents = contents
        self.possible_answers = []
        self.correct_answer = correct_answer


def fill_data(line, flag):
    if (flag != -1) and flag != 0:
        TEMPORARY_MEMORY[flag].append(line)
    if flag == 0 and not line.replace(' ', '') == '':
        TEMPORARY_MEMORY[flag].append(line.replace(' ', ''))

def check_end(line, flag, temp_line, start_for):

    options = defaultdict(lambda: False, {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True,})

    if temp_line.startswith('Question') and not start_for == True:
        print(TEMPORARY_MEMORY[1][0:1],' ', ''.join(TEMPORARY_MEMORY[0]))
        for _ in range(24):
            del TEMPORARY_MEMORY[_][:]
        flag = -1

    if ':' in ''.join(TEMPORARY_MEMORY[0]) and temp_line != '':
        print(options[temp_line[0]], '  ', temp_line[0])

        if not temp_line[0] == ',' and not temp_line[0] == 'A'and not temp_line[0] == 'B'and not temp_line[0] == 'C'and not temp_line[0] == 'D'and not temp_line[0] == 'E'and not temp_line[0] == 'F':

            if not TEMPORARY_MEMORY[0] == '':

                for _ in range(24):
                    del TEMPORARY_MEMORY[_][:]
                flag = -1
    return flag

def split_the_base_into_a_single_one(lines):
    # flag =-2 at start, flag = -1 for other flag = 0 for answers, flag = 1 for Question X, flag =2,3,4,5... for A,B,C,D...
    flag = -1
    data_base=[[] for _ in range(200)]
    for line in lines:
        temp_line = line.replace(' ', "")
        #flag = check_end(line,flag, temp_line,start_for)
        if temp_line.startswith('Question'):
            flag = 1
            print(data_base[flag])
            print('    ')
        data_base[flag].append(line)



        #fill_data(line, flag)



def import_data_from_file():
    pdf_file = open('123.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    lines = []
    #for page_now in range(1, 25):
    for page_now in range(read_pdf.getNumPages()):
        page_content = read_pdf.getPage(page_now).extractText()
        lines.extend(page_content.splitlines())
    # lines.extend(a for page_now in range(read_pdf.getNumPages()) for a in read_pdf.getPage(page_now).extractText().splitlines())
    return lines


def remove_page_number(lines):
    lines_now = []
    number_page_inside = 1

    for line in lines:
        temp_line = line.replace(' ', "")
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
        temp_line = line.replace(' ', "")
        if temp_line.startswith('Question'):
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
            if line.replace(' ', "") == wrong_lines.replace(' ', ""):
                flag = False
        if flag == True:
            lines_now.append(line)
        else:
            flag = True
    return lines_now


def delete_empy_lines_at_beginning_of_the_document(lines):
    while not lines[0].replace(' ', "").startswith('Question'):
        del lines[0]
    return lines

def delete_empy_lines_in_document(lines):
    lines_now = []
    for line in lines:
        if line == '':
            continue
        else:
            lines_now.append(line)
    return lines_now

if __name__ == '__main__':

    start= time.time()
    parser = argparse.ArgumentParser(description='Program for learning from script')
    parser.add_argument('-f', default='123.pdf')
    # , help='Write file name', required=True
    args = parser.parse_args()

    if args.f == 'Write file name':
        print('I can tell that no argument was given and I can deal with that here.')
    elif args.f == '123.pdf':
        print('Ok')
    else:
        print('I can not find it')

    lines = import_data_from_file()
    lines = remove_page_number(lines)
    lines = remove_section_page_footer(lines)
    lines = delete_empy_lines_at_beginning_of_the_document(lines)
    lines = delete_empy_lines_in_document(lines)

    split_the_base_into_a_single_one(lines)
    stop=time.time()

    print('The program worked for %.3f seconds' % (stop-start))


# divide_data_into_parts()
# allocate_data_to_class()
# randomize_numer_question()
# get_a_question()

'''
def fill_data(line, flag):
    if (flag != -1) and flag != 0:
        TEMPORARY_MEMORY[flag].append(line)
    if flag == 0 and not line.replace(' ', '') == '':
        TEMPORARY_MEMORY[flag].append(line.replace(' ', ''))

def check_end(line, flag, temp_line, start_for):

    options = defaultdict(lambda: False, {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True,})

    if temp_line.startswith('Question') and not start_for == True:
        print(TEMPORARY_MEMORY[1][0:1],' ', ''.join(TEMPORARY_MEMORY[0]))
        for _ in range(24):
            del TEMPORARY_MEMORY[_][:]
        flag = -1

    if ':' in ''.join(TEMPORARY_MEMORY[0]) and temp_line != '':
        print(options[temp_line[0]], '  ', temp_line[0])

        if not temp_line[0] == ',' and not temp_line[0] == 'A'and not temp_line[0] == 'B'and not temp_line[0] == 'C'and not temp_line[0] == 'D'and not temp_line[0] == 'E'and not temp_line[0] == 'F':

            if not TEMPORARY_MEMORY[0] == '':

                for _ in range(24):
                    del TEMPORARY_MEMORY[_][:]
                flag = -1
    return flag

def split_the_base_into_a_single_one(lines):
    # flag =-2 at start, flag = -1 for other flag = 0 for answers, flag = 1 for Question X, flag =2,3,4,5... for A,B,C,D...
    flag = -2
    start_for = True
    for line in lines:
        temp_line = line.replace(' ', "")
        flag = check_end(line,flag, temp_line,start_for)
        if temp_line.startswith('Question'):
            flag = 1
            #print(flag, ' ok3 ',line)
        if (
            temp_line.startswith('A.')
            or temp_line.startswith('B.')
            or temp_line.startswith('C.')
            or temp_line.startswith('D.')
            or temp_line.startswith('E.')
            or temp_line.startswith('F.')
            or temp_line.startswith('G.')
        ):
            flag += 1
            #print(flag, ' ok1 ',line)

        if temp_line.startswith('Answer:'):
            flag = 0
            #print(flag, ' ok ',line)
        if start_for == True:
            start_for = False
        fill_data(line, flag)
        # print(flag, line)
    print(''.join(TEMPORARY_MEMORY[0]))

'''