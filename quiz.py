#!/usr/bin/env python3

"""A program for learning content from a script"""
import time

from parser.parse import remove_clutter, parse_document
from parser.pdf_reader import read_pdf_file


def main():
    """Main program function"""
    start = time.time()
    # TODO: Read from cmd
    file_name = "123.pdf"
    doc = read_pdf_file(file_name)
    doc = remove_clutter(doc)
    questions = parse_document(doc)
    stop = time.time()
    print("The program worked for %.3f seconds" % (stop - start))
    for q in questions:
        print(q.question)
        for a in q.answers:
            print("\t{}".format(a))
    # start = time.time()
    # questions_memory = ask_question(question_memory, number_of_questions)
    # stop = time.time()
    # results(questions_memory, start, stop, number_of_questions)


if __name__ == "__main__":
    main()
