import tkinter as tk
from tkinter import *
import tkinter.font as font
import random

wwidth = 275
wheight = 320

computerChoices = ["rock", "paper", "scissors"]
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
    }

won = 0
lost = 0
played = 0

def playRock():
    global won
    global lost
    global played
    
    result = ""
    player = "rock"
    computer = random.choice(computerChoices)

    if computer == player:
        result = "You tied!"
    elif beats[player] == computer:
        result = "You won!"
        won+=1
    else:
        result = "You lost :("
        lost+=1

    played+=1
    label.config(text=result)
    label2.config(text=f"Computer chose {computer}.")

def playScissor():
    global won
    global lost
    global played
    
    result = ""
    player = "scissors"
    computer = random.choice(computerChoices)

    if computer == player:
        result = "You tied!"
    elif beats[player] == computer:
        result = "You won!"
        won+=1
    else:
        result = "You lost :("
        lost+=1

    played+=1
    label.config(text=result)
    label2.config(text=f"Computer chose {computer}.")

def playPaper():
    global won
    global lost
    global played
    
    result = ""
    player = "paper"
    computer = random.choice(computerChoices)

    if computer == player:
        result = "You tied!"
    elif beats[player] == computer:
        result = "You won!"
        won+=1
    else:
        result = "You lost :("
        lost+=1

    played+=1
    label.config(text=result)
    label2.config(text=f"Computer chose {computer}.")

def updateScores():
    scores.config(text=f"You {won}:{lost} Computer")
    playedtext.config(text=f"Played {played} games.")
    root.after(1, updateScores)

root = tk.Tk()

Label(root, text="").pack()

label  = Label(root, text="RPS");label.pack()
label2 = Label(root, text="Pick your move!");label2.pack()

Label(root, text="").pack()

btnRock    = Button(root, text="Rock",     width=20, height=1, command=playRock)
btnPaper   = Button(root, text="Paper",    width=20, height=1, command=playPaper)
btnScissor = Button(root, text="Scissors", width=20, height=1, command=playScissor)

btnRock['font']    = font.Font(family='Segoe UI', size=12)
btnPaper['font']   = font.Font(family='Segoe UI', size=12)
btnScissor['font'] = font.Font(family='Segoe UI', size=12)

label['font']  = font.Font(family='Segoe UI', size=22, weight=font.BOLD)
label2['font'] = font.Font(family='Segoe UI', size=14)

btnRock.pack()
btnPaper.pack()
btnScissor.pack()

Label(root, text="").pack()

scores     = Label(root, text="");scores.pack()
playedtext = Label(root, text="");playedtext.pack()

scores['font']     = font.Font(family='Segoe UI', size=10)
playedtext['font'] = font.Font(family='Segoe UI', size=10)

Label(root, text="").pack()

root.after(1, updateScores)
root.wm_title("Rock Paper Scissors")
root.geometry(f"{wwidth}x{wheight}")
root.mainloop()
