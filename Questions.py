#!/usr/bin/env python3

import PyPDF2
import time


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
                #print(lines[i])
                break
            elif lines[i][j:j + 2] == 'B.':
                flag = 1
                #print(lines[i])
                break

            elif lines[i][j:j + 2] == 'C.':
                flag = 1
                #print(lines[i])
                break
            elif lines[i][j:j + 2] == 'D.':
                flag = 1
                #print(lines[i])
                break

            elif lines[i][j:j + 2] == 'E.':
                flag = 1
                #print(lines[i])
                break
            elif lines[i][j:j + 2] == 'F.':
                flag = 1
                #print(lines[i])
                break
            elif lines[i][j:j + 7] == 'Answer:':
                flag = 1
                print(lines[i][j:j + 7])

                if lines[i][j + 7:].replace(' ', '').replace(',', '') == '':
                    print('Withonut correct answer', lines[i],lines[i+1],lines[i+2],lines[i+3])
                else:
                    print(lines[i][j + 7:].replace(' ', '').replace(',', ''))
                break

def import_data_from_file():
    pdf_file = open('123.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    lines = []
    '''
    #for page_now in range(1, 3):
    for page_now in range(read_pdf.getNumPages()):
        page_content = read_pdf.getPage(page_now).extractText()
        lines.extend(page_content.splitlines())
    '''
    lines.extend(a for page_now in range(1, 3) for a in read_pdf.getPage(page_now).extractText().splitlines())
    #lines.extend(a for page_now in range(read_pdf.getNumPages()) for a in read_pdf.getPage(page_now).extractText().splitlines())
    return(lines)

def remove_page_number(lines):
    lines_now = []
    number_page_inside = 1

    for line in lines:
        temp_line = line.replace(' ', '')
        if temp_line == str(number_page_inside):
            number_page_inside += 1
            continue
        else:
            lines_now.append(line)
    return (lines_now)

def end_of_loop():
    raise StopIteration

def remove_section_page_footer(lines):

    '''
    temp_lines = []
    for line in lines:  # lines before Question 1 contains something
        temp_line = line.replace(' ', '')
        if temp_line.startswith('Question'):
            break
        else:
            if temp_line != '':
                temp_lines.append(line)
    '''

    temp_lines= list(end_of_loop() if line.replace(' ', '').startswith('Question') else line for line in lines)
    return (delete_page_footer(lines, temp_lines))

def delete_page_footer(lines,temp_lines):
    lines_now = []
    flag = 1
    for line in lines:
        for wrong_lines in temp_lines:
            if line.replace(' ', '') == wrong_lines.replace(' ', ''):
                flag = 0
        if flag == 1:
            lines_now.append(line)
        else:
            flag = 1
    return(lines_now)



if __name__ == '__main__':

    lines = import_data_from_file()
    lines = remove_page_number(lines)
    start = time.time()
    lines = remove_section_page_footer(lines)
    end = time.time()
    print(end-start)
    #fill_data(lines)


#print(lines_now)
#for line in temp_lines: # lines before Question contains something

#print(temp_lines, len(temp_lines))
#fill_data(lines)





#read_name_file()
#delete_numer_page()
#delete_section_page_footer()
#divide_data_into_parts()
#allocate_data_to_class()
#randomize_numer_question()
#get_a_question()
'''




'''