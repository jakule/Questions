#!/usr/bin/env python3

"""A program for learning content from a script"""
import argparse
import time

from parser.exporter import save_as_json
from parser.parse import remove_clutter, parse_document
from parser.pdf_reader import read_pdf_file


def main():
    """Main program function"""
    parser = argparse.ArgumentParser(description="Process some stuff....")
    parser.add_argument(
        "-f,--file", dest="file", help="The name of input file", required=True
    )
    parser.add_argument(
        "--save", action="store_false", help="Save processed file to json file"
    )
    args = parser.parse_args()

    start = time.time()
    file_name = args.file
    doc = read_pdf_file(file_name)
    doc = remove_clutter(doc)
    questions = parse_document(doc)
    stop = time.time()

    print("The program worked for %.3f seconds" % (stop - start))

    # TODO add option to read from this file
    if args.save:
        save_as_json("db.json", questions)

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
