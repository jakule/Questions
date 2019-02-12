from typing import List

from attr import dataclass


@dataclass
class Question:
    """ Struct describing a question """

    question: str
    answers: List[str]
    correct_answer: int
