from tkinter import Button, Label, Entry

class Question:

    def __init__(self, question_text, window):
        self.question_text = question_text
        self.window = window
        self.answer_check_button = Button(self.window, text="Check Answers", command=self.check_answers)
        self.win_label = Label(self.window, text="Good Job. You got them all")
        self.level_title_label = Label(self.window, text=self.question_text)
        self.question_answered = False

    def display_win_label(self):

        self.win_label.grid(column=2, row=len(self.answers) + 2)
        self.question_answered = True

class MultipleChoice(Question):
    pass

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
            self.labels.append(Label(self.window, text=f"{self.layer_level_text} {count} of {self.topic_label_text}"))
            self.labels[count-1].grid(column=1, row=count)

            self.entries.append(Entry(self.window))
            self.entries[count-1].grid(column=2, row=count)

            count += 1

            self.answer_check_button.grid(column=2, row=len(self.entries) + 1)

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
        while en < len(self.entries):
            
            if self.entries[en].get() == self.answers[en] or self.entries[en].get().lower() == self.answers[en].lower():

                self.answer_check_labels.insert(en, Label(self.window, text="Correct"))
                en += 1
            else:
                self.answer_check_labels.insert(en, Label(self.window, text="Incorrect"))
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
            self.display_win_label()

class UnorderedFillInTheBlank(Question):

    pass