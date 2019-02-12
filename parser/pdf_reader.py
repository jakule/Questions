import io

import PyPDF2


def read_pdf_file(file_name: str) -> str:
    """Read PDF file and return while document as single string"""
    pdf_file = open(file_name, "rb")
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    doc = io.StringIO()
    for page_now in range(read_pdf.getNumPages()):
        page_content: str = read_pdf.getPage(page_now).extractText()
        page_content = page_content.strip(" \n")
        if page_content:
            doc.write(page_content)
    return doc.getvalue()
