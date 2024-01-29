import tkinter
from guesslevelgenerator import GenerateLevel
from gamemanager import GameManager

guess_game_window = tkinter.Tk()
guess_game_window.title("Name IT terms")
guess_game_window.minsize(width=500, height=300)

def start_game(game):
    welcome_button.destroy()
    welcome_label.destroy()
    game.start_game()

osi_level = GenerateLevel(7, "Name all of the OSI layers", "the OSI Model", "Layer", ["Physical", "Data Link", "Network", "Transportation", "Session", "Presentation", "Application"], guess_game_window)

tcp_ip_level = GenerateLevel(4, "Name all of the TCP/IP layers", "the TCP/IP model", "Layer", ["Network Access", "Internet", "Transport", "Application"], guess_game_window)
encapsulation = GenerateLevel(7, "Name the PDU at each level", "the OSI Model", "Layer", ["Bit", "Frame", "Packet", "Segment", "Data", "Data", "Data"], guess_game_window)
tcp_udp = GenerateLevel(2, "The two main layer four protocols from a to z", "2", "Layer Four protocol", ["TCP", "UDP"], guess_game_window)

game = GameManager([osi_level, tcp_ip_level,encapsulation,tcp_udp], guess_game_window)

welcome_label = tkinter.Label(guess_game_window, text="Welcome to the IT terms quiz")
welcome_label.pack()

welcome_button = tkinter.Button(guess_game_window, text="Start Quiz", command=lambda: start_game(game))
welcome_button.pack()

guess_game_window.mainloop()




