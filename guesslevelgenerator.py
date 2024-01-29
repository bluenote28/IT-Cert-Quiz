import tkinter


class GenerateLevel:

    def __init__(self, number_of_answers, title_text, topic_label_text, layer_level_text, answers, window):
        self.number_of_answers = number_of_answers
        self.title_text = title_text
        self.topic_label_text = topic_label_text
        self.layer_level_text = layer_level_text
        self.window = window
        self.level_title_label = tkinter.Label(self.window, text=self.title_text)
        self.answer_check_button = tkinter.Button(self.window, text="Check Answers", command=self.check_answers)
        self.labels = []
        self.entries = []
        self.answers = answers
        self.answer_check_labels = []
        self.level_over = False
        self.win_label = tkinter.Label(self.window, text="Good Job. You got them all")

    def setup_level(self):
        self.level_title_label.grid(column=2, row=0)

        count = 1

        while count <= self.number_of_answers:
            self.labels.append(tkinter.Label(self.window, text=f"{self.layer_level_text} {count} of {self.topic_label_text}"))
            self.labels[count-1].grid(column=1, row=count)

            self.entries.append(tkinter.Entry(self.window))
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

        if correct_answers == self.number_of_answers:
            self.display_win_label()

    def display_win_label(self):

        self.win_label.grid(column=2, row=self.number_of_answers + 2)
        self.level_over = True





