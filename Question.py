# BJC, Original Author
# 3/1/2024

# Question Class that organizes the questions I am quizzing the user with

class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def display(self):
        print(self.text)
        for i, choice in enumarate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, answer):
        return answer == self.correct_answer
