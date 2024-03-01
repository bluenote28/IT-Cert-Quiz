import tkinter
from question import OrderedFillInTheBlank, MultipleChoice
from awssolutionsarchitect import AWSSolutionsArchitect

quiz_window = tkinter.Tk()
quiz_window.title("Name IT terms")
quiz_window.minsize(width=500, height=300)
current_question_index = 0


aws_solutions_architect = AWSSolutionsArchitect(quiz_window)
questions = aws_solutions_architect.questions

welcome_label = tkinter.Label(quiz_window, text="Welcome to the IT terms quiz")
welcome_label.pack()

def check_question():
    global current_question_index

    if not questions[current_question_index].question_displayed and current_question_index < len(questions):
        current_question_index += 1
        questions[current_question_index].display_question()

    quiz_window.after(1, check_question)

def display_question():

    welcome_button.destroy()
    welcome_label.destroy()
    
    questions[current_question_index].display_question()
    quiz_window.after(1, check_question)


welcome_button = tkinter.Button(quiz_window, text="Start Quiz", command=display_question)
welcome_button.pack()

quiz_window.mainloop()




