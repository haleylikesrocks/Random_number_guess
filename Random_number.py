from tkinter import * #for gui
import random #for randon numbers


# setting the number of attemps to zero at teh beginning of each game
# global attempts
# attempts=0

def check_range():
    messaging=Label(root, text='')
    messaging.pack
    
    try:
        global low_range
        low_range= int(low_box.get())
        global high_range
        high_range= int(high_box.get())
        if low_range<high_range:
            messaging.config(text="Okay the range is set")
            messaging.pack
            chcker.pack_forget()
            low_box.pack_forget()
            high_box.pack_forget()
            higher.pack_forget()
            lower.pack_forget()
            ranger_ask.pack_forget()
            guess_a_num()
            # global guess_time
            # guess_time = Button(frame,
            #         text="Ready to guess!",
            #         font = ("Comic Sans MS", 26, "bold"),
            #         bg='green',
            #            command=guess_a_num)
            # guess_time.pack(pady=10)
    except ValueError:
        messaging.config(text="Enter a number you ding dong")
    messaging.pack


    
    
# setting up the game play
def set_range():
    start.pack_forget()
    instructions.pack_forget()
    range_ask="Please enter the lower number of the range in the first box and the higher number of the range in the second:"
    global ranger_ask
    ranger_ask= Label(root, text=range_ask)
    ranger_ask.pack(pady=20)
    global lower
    lower=Label(root, text="Low Number")
    lower.pack(padx=10)
    global low_box
    low_box = Entry(root)
    low_box.pack(pady=10)
    global high_box
    global higher
    higher=Label(root, text="High Number")
    higher.pack(padx=10)
    high_box = Entry(root)
    high_box.pack(pady=10)
    global chcker 
    chcker = Button(frame,
                text="Submit",
                font = ("Comic Sans MS", 26, "bold"),
                bg='green',
               	command=check_range)
    chcker.pack(pady=10)
    
def guess_a_num():
    global number_goal
    number_goal=random.randint(low_range, high_range)
    prompt="Guess a number between {low} and {high}".format(low=low_range, high=high_range)
    prompting=Label(root, font = ("Comic Sans MS", 26, "bold"), text=prompt)
    prompting.pack(padx=20)
    global guess_box
    guess_box = Entry(root)
    guess_box.pack(pady=10)
    enter_guess =Button (frame,
                    text="Submit guess",
                    font = ("Comic Sans MS", 26, "bold"),
                    bg='green',
                    command=check_guess)
    enter_guess.pack(pady=10)
    global attempts
    attempts+=1

# def good_bye():
#     bye="Hope you had a bit of fun! Bye bye!"
#     byeee=label(root, font=("Comic Sans MS", 26, "bold"), text=bye)
#
def check_guess():
    try:
        number_guess = int(guess_box.get())
    except ValueError:
        print("nope")
#     if number_guess==number_goal:
#         congrats=" Well done! You\'ve guessed the number! It took you {attempts} attempts. Think you can do better?"
#         guessed_right= label(root, font=("Comic Sans MS", 26, "bold"), text=message)
#         yes=  Button (frame,
#                 text="Yes! Play again",
#                 bg='LightBlue',
#                 fg='LightBlue',
#                 font = ("Comic Sans MS", 26, "bold"),
#                 command=set_range)
#         no =  Button (frame,
#                 text="No, I'm done",
#                 bg='LightBlue',
#                 fg='LightBlue',
#                 font = ("Comic Sans MS", 26, "bold"),
#                 command=goodbye)
#         guessed_right= label(root, font=("Comic Sans MS", 26, "bold"), text=message)
#

# setting up the window

root = Tk()
frame = Frame(root)
frame.pack()
global attempts
attempts=0
print (attempts)
start= Button (frame,
				text="Start",
				bg='LightBlue',
				fg='LightBlue',
				font = ("Comic Sans MS", 26, "bold"),
				command=set_range)
start.pack(side=LEFT)


instruct="Welcome to my Random Number Generator"+'\n'+"Choose a range and then try to guess the number that has been randomly choosen."+'\n'+"Don't worry we will make sure to tell you if the number is lower or higher than your guess."+'\n'+'Makey sure that you guess a number that is actually in the range' + '\n' +'Don\'t worry we\'ll keep track of your attemps.'+'\n'+'Have Fun!'
instructions=Label(root, font = ("Comic Sans MS", 26, "bold"), text=instruct)
instructions.pack()

root.mainloop()
