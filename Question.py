# BJC, Original Author
# 3/1/2024

# Question Class that organizes the questions I am quizzing the user with
# Also includes loading function for all of the questions

class Question:
    def __init__(self, text, choices, correct_answer, category, difficulty):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer
        self.category = category
        self.difficulty = difficulty

    def display(self):
        print(self.text)
        for i, choice in enumarate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, answer):
        return answer == self.correct_answer

def load_questions_from_json(file_path):
    with open(file_path, "r") as file:
        questions_data = json.load(file)

    questions = []
    for question_data in questions_data:
        question = Question(question_data["text"], question_data["choices"], question_data["correct_answer"], question_data["subject"]), question_data["difficulty"])
        questions.append(question)
    return questions
