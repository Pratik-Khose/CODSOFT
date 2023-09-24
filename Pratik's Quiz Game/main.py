import json
import tkinter as tk
from tkinter import messagebox as mb

print("Enjoy your Quiz Game !!!")
print("HAVE FUN !!!")
class MyQuiz:
    def __init__(self, root):
        self.root = root
        self.root.geometry("850x450")
        self.root.title("Pratik's Quiz Game")
        self.quesNumber = 0
        self.score = 0

        with open('questions.json') as json_file:
            data = json.load(json_file)

        self.questions = data['ques']
        self.options = data['choices']
        self.answers = data['ans']

        self.optSelected = tk.IntVar()

        self.displayTitle()
        self.question_label = self.displayQuestion()
        self.radioButtons()
        self.displayOptions()
        self.buttons()

    def displayResult(self):
        result_message = f"You scored {self.score}/{len(self.questions)} correct answers!"
        mb.showinfo("Quiz Result", result_message)

    def checkAnswer(self, quesNumber):
        selected_answer = self.optSelected.get()

        if selected_answer == self.answers[quesNumber]:
            return True
        else:
            return False

    def nextButton(self):
        if self.checkAnswer(self.quesNumber):
            self.score += 1

        self.quesNumber += 1

        if self.quesNumber == len(self.questions):
            self.displayResult()
            self.root.destroy()
        else:
            self.displayQuestion()
            self.displayOptions()

    def buttons(self):
        next_button = tk.Button(
            self.root,
            text="Next",
            command=self.nextButton,
            width=10,
            bg="green",
            fg="white",
            font=("Comic Sans MS", 16, "bold")
        )
        next_button.place(x=350, y=380)

        quit_button = tk.Button(
            self.root,
            text="Quit",
            command=self.root.destroy,
            width=5,
            bg="red",
            fg="white",
            font=("Comic Sans MS", 16, " bold")
        )
        quit_button.place(x=700, y=380)

    def displayOptions(self):
        for i in range(4):
            self.options_radio[i]['text'] = self.options[self.quesNumber][i]

    def displayQuestion(self):
        question_label = tk.Label(
            self.root,
            text=self.questions[self.quesNumber],
            width=100,
            font=("Comic Sans MS", 16, 'bold'),
            anchor='w'
        )
        question_label.place(x=50, y=100)
        return question_label

    def displayTitle(self):
        myTitle = tk.Label(
            self.root,
            text="QUIZ",
            width=50,
            fg="black",
            font=("Comic Sans MS", 25, "bold"),
            anchor = 'w'
        )
        myTitle.place(x=50, y=0)

    def radioButtons(self):
        self.options_radio = []
        y_pos = 150

        for i in range(4):
            radio_button = tk.Radiobutton(
                self.root,
                text="",
                variable=self.optSelected,
                value=i + 1,
                font=("Comic Sans MS", 14)
            )
            self.options_radio.append(radio_button)
            radio_button.place(x=100, y=y_pos)
            y_pos += 40

root = tk.Tk()
quiz = MyQuiz(root)
root.mainloop()
