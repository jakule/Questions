#!/usr/bin/env python3

import PyPDF2
import collections


class Question:
    def __init__(self, id, contents, correct_answers):
        self.id = id
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



if __name__ == '__main__':


    pdf_file = open('123.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    c = number_of_pages
    for page_now in range(1,5):
        page = read_pdf.getPage(page_now)
        page_content = page.extractText()

        lines = page_content.splitlines()
        fill_data(lines)
        #print (page_content)



