from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)
        true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.press_true)
        self.true.grid(column=0, row=2, pady=30)
        false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.press_false)
        self.false.grid(column=1, row=2, pady=30)
        self.score = Label(text="Score: 0", font=("arial", 10, "bold"), bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, pady=30)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="End")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
            messagebox.showinfo(title="Trivia Complete", message=f"You Scored {self.quiz.score}/10")

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def press_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
