from typing import List


class Question:
    """ Struct describing a question """

    question: str
    answers: List[str]
    correct_answer: int
