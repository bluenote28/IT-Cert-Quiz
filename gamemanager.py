import tkinter

class GameManager:

    def __init__(self, levels, window):
        self.levels = levels
        self.window = window
        self.end_screen = tkinter.Label(self.window, text="You have reached the end. Congrats!!")
        self.level_count = len(levels)
        self.current_question_index = 0

    def start_game(self):

        current_question = self.levels[self.current_question_index]
        current_question.display_question()
        print(current_question.question_displayed)
        current_question.destroy_question()
        print(current_question.question_displayed)

        #while self.current_question_index < self.level_count:
        #while current_question.question_displayed:
        #    print(self.current_question_index)

        #maybe put all this in main#######
            
