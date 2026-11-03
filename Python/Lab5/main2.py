class Question:
    def __init__(self, text, points):
        self.text = text
        self.points = points
    def check(self,answer):
        pass
    def __str__(self):
        return f"{self.text} points: {self.points}"

class SingleChoiceQuestion(Question):
    def __init__(self, text, points,options:list[str],correct_answer:str):
        super().__init__(text, points)
        self.options = options
        self.correct_answer = correct_answer
    def check(self, answer):
        if answer == self.correct_answer:
            return True
        return False

class MultipleChoiceQuestion(Question):
    def __init__(self, text, points,options:list[str],correct_answers:list[str]):
        super().__init__(text, points)
        self.options = options
        self.correct_answers = correct_answers

    def check(self, answer):
        if set(answer) == set(self.correct_answers):
            return True
        return False

class OpenQuestion(Question):
    def __init__(self, text, points,correct_answer:str):
        super().__init__(text, points)
        self.correct_answer = correct_answer
    def check(self, answer):
        if answer.lower() == self.correct_answer.lower():
            return True
        return False

class Quiz:
    def __init__(self, title, questions:list[Question]):
        self.title = title
        self.questions = questions
    def add_question(self, question:Question):
        self.questions.append(question)
    def evaluate(self,answers):
        total = 0
        total_possible = 0
        for question,answer in zip(self.questions,answers):
            if question.check(answers):
                total += question.points
            total_possible += question.points
        return total, total_possible

