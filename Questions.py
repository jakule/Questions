
class BaseQuestions:
    def __init__(self,id,question,answerA,answerB,answerC,answerD,correctAnswer):
        self.id = id
        self.question = question
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD
        self.correctAnswer = correctAnswer

    def getId(self):
        return self.id

    def getQuestion(self):
        return self.question

    def getAnswerA(self):
        return self.answerA

    def getAnswerB(self):
        return self.answerB

    def getAnswerC(self):
        return self.answerC

    def getAnswerD(self):
        return self.answerD

    def getCorrectAnswer(self):
        return self.correctAnswer


if __name__ == '__main__':
    print('first commit')
