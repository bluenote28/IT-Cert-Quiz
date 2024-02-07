import tkinter
from gamemanager import GameManager
from question import OrderedFillInTheBlank, MultipleChoice

guess_game_window = tkinter.Tk()
guess_game_window.title("Name IT terms")
guess_game_window.minsize(width=500, height=300)

def start_game(game):
    welcome_button.destroy()
    welcome_label.destroy()
    game.start_game()

osi_question = OrderedFillInTheBlank(guess_game_window, "Name all of the layers of the OSI Model", ["Physical", "Data Link", "Network", "Transportation", "Session", "Presentation", "Application"], "Layer", "the OSI model")
##encapsulation = OrderedFillInTheBlank(guess_game_window, "Name the PDU at each level", ["Bit", "Frame", "Packet", "Segment", "Data", "Data", "Data"], "the OSI Model", "Layer")
##tcp_udp = GenerateLevel(2, "The two main layer four protocols from a to z", "2", "Layer Four protocol", ["TCP", "UDP"], guess_game_window)
##man_question = MultipleChoice(guess_game_window, "Which network type covers a city wide area?", ['LAN', 'WAN', 'PAN', 'MAN'], 3)

game = GameManager([osi_question], guess_game_window)

welcome_label = tkinter.Label(guess_game_window, text="Welcome to the IT terms quiz")
welcome_label.pack()

welcome_button = tkinter.Button(guess_game_window, text="Start Quiz", command=lambda: start_game(game))
welcome_button.pack()

guess_game_window.mainloop()




