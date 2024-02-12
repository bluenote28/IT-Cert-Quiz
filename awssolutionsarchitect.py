import tkinter
from question import OrderedFillInTheBlank, MultipleChoice

quiz_window = tkinter.Tk()
quiz_window.title("Name IT terms")
quiz_window.minsize(width=500, height=300)
current_question_index = 0

osi_question = OrderedFillInTheBlank(quiz_window, "Name all of the layers of the OSI Model", ["Physical", "Data Link", "Network", "Transportation", "Session", "Presentation", "Application"], "Layer", "the OSI model")
encapsulation = OrderedFillInTheBlank(quiz_window, "Name the PDU at each level", ["Bit", "Frame", "Packet", "Segment", "Data", "Data", "Data"], "the OSI Model", "Layer")
##tcp_udp = GenerateLevel(2, "The two main layer four protocols from a to z", "2", "Layer Four protocol", ["TCP", "UDP"], guess_game_window)
##man_question = MultipleChoice(guess_game_window, "Which network type covers a city wide area?", ['LAN', 'WAN', 'PAN', 'MAN'], 3)

questions = [osi_question, encapsulation]

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
