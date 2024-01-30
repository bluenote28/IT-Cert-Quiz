import tkinter
import tkinter.messagebox

class GameManager:

    def __init__(self, levels, window):
        self.levels = levels
        self.window = window
        self.end_screen = tkinter.Label(self.window, text="You have reached the end. Congrats!!")
        self.level_count = len(levels)
        self.next_level_button = tkinter.Button(self.window, text="Next Level", command=self.destroy_level)
        self.current_level = 0

    def add_level(self, level):
        self.levels.append(level)

    def start_game(self):
        self.levels[self.current_level].display_question()
        self.next_level_button.grid(column=3, row=len(self.levels[self.current_level].answers) + 1)

    def start_next_level(self):
        if self.current_level >= self.level_count:
            self.next_level_button.destroy()
            self.end_screen.pack()
        else:
            self.levels[self.current_level].display_question()
            self.next_level_button.grid(column=3, row=len(self.levels[self.current_level].answers) + 1)

    def destroy_level(self):

        message = tkinter.messagebox
        
        if self.levels[self.current_level].question_answered:

            count = 0

            while count < len(self.levels[self.current_level].answers):
                self.levels[self.current_level].answer_check_labels[count].destroy()
                count += 1
            self.levels[self.current_level].answer_check_labels.clear()

            for label in self.levels[self.current_level].labels:
                label.destroy()

            for entry in self.levels[self.current_level].entries:
                entry.destroy()

            self.levels[self.current_level].answer_check_button.destroy()
            self.levels[self.current_level].win_label.destroy()
            self.levels[self.current_level].level_title_label.destroy()
            self.current_level += 1
            self.start_next_level()
        else:
            message.showerror(title="Warning", message="You have not answered all questions correctly.", parent=self.window)
        

