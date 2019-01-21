#!/usr/bin/env python3

import PyPDF2
import collections


class Question:
    def __init__(self, contents, correct_answer):
        self.contents = contents
        self.possible_answers = []
        self.correct_answer = correct_answer


def fill_data(lines):
    flag =0
    for i in range(len(lines)):
        for j in range(2):
            if lines[i][j:j + 8] == 'Question':
                flag = 1
                print(lines[i])
                break
            elif lines[i][j:j + 2] == 'A.':
                flag = 1
                print(lines[i])
                break
            elif lines[i][j:j + 2] == 'B.':
                flag = 1
                print(lines[i])
                break

            elif lines[i][j:j + 2] == 'C.':
                flag = 1
                print(lines[i])
                break
            elif lines[i][j:j + 2] == 'D.':
                flag = 1
                print(lines[i])
                break

            elif lines[i][j:j + 2] == 'E.':
                flag = 1
                print(lines[i])
                break
            elif lines[i][j:j + 2] == 'F.':
                flag = 1
                print(lines[i])
                break
            elif lines[i][j:j + 7] == 'Answer:':
                flag = 1
                print(lines[i][j:j + 7])

                if lines[i][j + 7:].replace(' ', '').replace(',', '') == '':
                    print('Withonut correct answer')
                else:
                    print(lines[i][j + 7:].replace(' ', '').replace(',', ''))
                break

def import_data_from_file():
    pdf_file = open('123.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    c = number_of_pages
    lines = ['']
    for page_now in range(1, 5):
        # for page_now in range(read_pdf.getNumPages()):
        page = read_pdf.getPage(page_now)
        page_content = page.extractText()
        lines = lines + page_content.splitlines()
    return(lines)

if __name__ == '__main__':


    lines = import_data_from_file()
    temp_lines= []
    for line in lines: #every line before Question 1 contains something
        temp_line = line.replace(' ','')
        if temp_line.startswith('Question'):
            break
        else:
            if temp_line != '':
                temp_lines.append(line)
    #for line in temp_lines: # lines before Question contains something

    print(temp_lines, len(temp_lines))
    fill_data(lines)





    #read_name_file()
    #delete_numer_page()
    #delete_section_page_footer()
    #divide_data_into_parts()
    #allocate_data_to_class()
    #randomize_numer_question()
    #get_a_question()