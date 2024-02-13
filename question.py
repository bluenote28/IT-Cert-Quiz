import tkinter
import tkinter.messagebox

class Question:

    def __init__(self, question_text, window):
        self.question_text = question_text
        self.window = window
        self.answer_check_button = tkinter.Button(self.window, text="Submit", command=self.check_answers)
        self.next_level_button = tkinter.Button(self.window, text="Next Question", command=self.destroy_question)
        self.win_label = tkinter.Label(self.window, text="Good Job. You got them all")
        self.level_title_label = tkinter.Label(self.window, text=self.question_text)
        self.question_answered = False
        self.question_displayed = False

    def display_win_label(self):

        self.win_label.grid(column=2, row=len(self.answers) + 2)
        self.question_answered = True

class MultipleChoice(Question):

    def __init__(self, window, question_text, answers, correct_answer):
        super(MultipleChoice, self).__init__(question_text, window)
        self.answers = answers
        self.correct_answer = correct_answer
        self.answer_buttons = []
        self.choice = tkinter.StringVar()
        self.display_answer_check = tkinter.Label(self.window, text="")


    def display_question(self):
        self.level_title_label.pack()

        for count, value in enumerate(self.answers):
            self.answer_buttons.append(tkinter.Radiobutton(self.window, text=value, variable=self.choice, value=self.answers[count]))
            self.answer_buttons[count].pack()

        self.answer_check_button.pack()
        self.next_level_button.pack()
        self.question_displayed = True

    def check_answers(self):
        
        if self.choice.get() == self.answers[self.correct_answer]:
            self.display_answer_check.config(text="Correct")
            self.question_answered = True
        else:
            self.display_answer_check.config(text="Incorrect")

        self.display_answer_check.pack()

    def destroy_question(self):

        self.level_title_label.destroy()
        self.answer_check_button.destroy()
        self.next_level_button.destroy()
        self.display_answer_check.destroy()

        for button in self.answer_buttons:
            button.destroy()

        self.question_displayed = False
       

class OrderedFillInTheBlank(Question):

    def __init__(self, window, question_text, answers, layer_level_text, topic_label_text):
        super(OrderedFillInTheBlank, self).__init__(question_text, window)
        self.answers = answers
        self.labels = []
        self.entries = []
        self.answer_check_labels = []
        self.layer_level_text = layer_level_text
        self.topic_label_text = topic_label_text


    def display_question(self):

        self.level_title_label.grid(column=2, row=0)

        count = 1

        while count <= len(self.answers):
            self.labels.append(tkinter.Label(self.window, text=f"{self.layer_level_text} {count} of {self.topic_label_text}"))
            self.labels[count-1].grid(column=1, row=count)

            self.entries.append(tkinter.Entry(self.window))
            self.entries[count-1].grid(column=2, row=count)

            count += 1

            self.answer_check_button.grid(column=2, row=len(self.answers) + 1)
            self.next_level_button.grid(column=3, row=len(self.answers) + 1)
        self.question_displayed = True

    def check_answers(self):

        ##detects if answer check lables are still on screen and removes them
        if len(self.answer_check_labels) != 0:
           i = 0
           while i < len(self.answer_check_labels):
            self.answer_check_labels[i].destroy()
            i += 1
        self.answer_check_labels.clear()

        ##checks answers and builds check answers list
        en = 0
        while en < len(self.answers):
            
            if self.entries[en].get() == self.answers[en] or self.entries[en].get().lower() == self.answers[en].lower():

                self.answer_check_labels.insert(en, tkinter.Label(self.window, text="Correct"))
                en += 1
            else:
                self.answer_check_labels.insert(en, tkinter.Label(self.window, text="Incorrect"))
                en += 1

        ##outputs correct or incorrect labels
        i = 0
        while i < len(self.answer_check_labels):
            self.answer_check_labels[i].grid(column=3, row=i + 1)
            i += 1

        ##check for if all answers are correct
        correct_answers = 0
        for label in self.answer_check_labels:
            if label.cget("text") == "Correct":
                correct_answers += 1

        if correct_answers == len(self.answers):
            self.question_answered = True
            self.display_win_label()

    def destroy_question(self):
        message = tkinter.messagebox
        
        if self.question_answered:

            count = 0

            while count < len(self.answers):
                self.answer_check_labels[count].destroy()
                count += 1
            self.answer_check_labels.clear()

            for label in self.labels:
                label.destroy()

            for entry in self.entries:
                entry.destroy()

            self.answer_check_button.destroy()
            self.win_label.destroy()
            self.level_title_label.destroy()
            self.next_level_button.destroy()

        else:
            message.showerror(title="Warning", message="You have not answered all questions correctly.", parent=self.window)
        
        self.question_displayed = False
        
class TrueOrFalse(Question):
    def __init__(self, window,question_text, answer):
        super().__init__(question_text, window)
        self.answer = answer
        self.answers = ['TRUE', 'FALSE']
        self.answer_buttons = []
        self.choice = tkinter.StringVar()
        self.display_answer_check = tkinter.Label(self.window, text="")

    def display_question(self):
        self.level_title_label.pack()

        for count, value in enumerate(self.answers):
            self.answer_buttons.append(tkinter.Radiobutton(self.window, text=value, variable=self.choice, value=self.answers[count]))
            self.answer_buttons[count].pack()

        self.answer_check_button.pack()
        self.next_level_button.pack()
        self.question_displayed = True
    def check_answers(self):
        
        if self.choice.get() == self.answers[self.correct_answer]:
            self.display_answer_check.config(text="Correct")
            self.question_answered = True
        else:
            self.display_answer_check.config(text="Incorrect")

        self.display_answer_check.pack()

    def destroy_question(self):

        self.level_title_label.destroy()
        self.answer_check_button.destroy()
        self.next_level_button.destroy()
        self.display_answer_check.destroy()

        for button in self.answer_buttons:
            button.destroy()

        self.question_displayed = False        

class UnorderedFillInTheBlank(Question):

    pass
