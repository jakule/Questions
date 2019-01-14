






if __name__ == '__main__':

    import PyPDF2
    import collections

    pdf_file = open('123.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    c = number_of_pages
    page = read_pdf.getPage(1)
    page_content = page.extractText()
    print (page_content)
    print(c)
    
