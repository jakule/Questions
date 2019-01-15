



def fill_data(lines):
    x=0
    flag =0
    for i in range(len(lines)):
        if lines[i] == 'Question 1':
            flag = 1
            print(lines[i])
            continue
        elif lines[i] == 'A.':
            flag = 1
            print(lines[i])
            continue
        elif lines[i] == 'B.':
            flag = 1
            print(lines[i])
            continue
        elif lines[i] == 'C.':
            flag = 1
            print(lines[i])
            continue
        elif lines[i] == 'D.':
            flag = 1
            print(lines[i])
            continue
        elif lines[i] == 'E.':
            flag = 1
            print(lines[i])
            continue
        elif lines[i] in 'Answer':
            flag = 1
            print(lines[i])
            continue

        x=x+1
    print(x)


if __name__ == '__main__':

    import PyPDF2
    import collections

    pdf_file = open('123.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    c = number_of_pages
    page = read_pdf.getPage(1)
    page_content = page.extractText()

    lines = page_content.splitlines()
    d = len(lines)

    flag = 1
    fill_data(lines)


    print(lines)
    #print (page_content)
    print(c)
    print(d)

