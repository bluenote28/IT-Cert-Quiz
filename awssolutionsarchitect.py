import tkinter
from question import OrderedFillInTheBlank, MultipleChoice

quiz_window = tkinter.Tk()
quiz_window.title("Name IT terms")
quiz_window.minsize(width=500, height=300)
current_question_index = 0

ondemand = MultipleChoice(quiz_window, "Which EC2 instance type lets you pay for what you use with no commitment?", ["spot", "on demand", "reserved","dedicated"], 1)
elastic = MultipleChoice(quiz_window, "Which type of IP address is a fixed public IP address for your EC2 instance?", ["public", "elastic", "private", "dynamic"] 1)
placement = MultipleChoice(quiz_window, "What is used to defined an EC2 placement strategy?" ['iam group', 'vpc subnet', 'ec2 clusters', 'placement group'], 3)
cluster_group = MultipleChoice(quiz_window, "Which placement strategy clusters instances into low latency group in a single AZ?", ['clusters','high availability','spread','partition'], 0)
spread_group = MultipleChoice(quiz_window, "Which placement strategy spreads instances across underlying hardware?", ['clusters','high availability','spread','partition'], 2)
partition_group = MultipleChoice(quiz_window, "Which placement strategy spreads many instances across different racks?", ['clusters','high availability','spread','partition'], 3)
partition_group_lat = MultipleChoice(quiz_window, "Which placement strategy has the lowest latencdy?", ['clusters','high availability','spread','partition'], 0)
spread_max = MultipleChoice(quiz_window, "What is the maximum number of instances possible in a spread placement group?", ['6','7','8','9'], 1)




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
