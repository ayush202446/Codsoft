from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageOps
from random import randint
import os

# Get the current working directory
cwd = os.getcwd()

# Function to create rounded images
def make_circle(image, size):
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    output = ImageOps.fit(image, (size, size))
    output.putalpha(mask)
    return ImageTk.PhotoImage(output)

# Main window
root = Tk()
root.title("Rock Paper Scissor Game")
root.configure(background="black")

# Resize the image using resize() method
resize_image1 = Image.open(os.path.join(cwd, "rock_user.png")).resize((200, 200))
resize_image2 = Image.open(os.path.join(cwd, "paper_user.png")).resize((200, 200))
resize_image3 = Image.open(os.path.join(cwd, "scissor_user.png")).resize((200, 200))
resize_image4 = Image.open(os.path.join(cwd, "rock_computer.png")).resize((200, 200))
resize_image5 = Image.open(os.path.join(cwd, "paper_computer.png")).resize((200, 200))
resize_image6 = Image.open(os.path.join(cwd, "scissor_computer.png")).resize((200, 200))

# Create rounded images
rock_user = make_circle(resize_image1, 200)
paper_user = make_circle(resize_image2, 200)
scissor_user = make_circle(resize_image3, 200)
rock_computer = make_circle(resize_image4, 200)
paper_computer = make_circle(resize_image5, 200)
scissor_computer = make_circle(resize_image6, 200)

# Insert image
user_label = Label(root, image=paper_user, bg="black")
computer_label = Label(root, image=paper_computer, bg="black")
computer_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
playerScore = Label(root, text=0, font=("Helvetica", 100), bg="black", fg="white")
computerScore = Label(root, text=0, font=("Helvetica", 100), bg="black", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, font=("Helvetica", 50), text="USER", bg="black", fg="white")
user_indicator.grid(row=0, column=3)
computer_indicator = Label(root, font=("Helvetica", 50), text="COMPUTER", bg="black", fg="white")
computer_indicator.grid(row=0, column=1)

# Result feedback messages
msg = Label(root, font=("Helvetica", 50), bg="black", fg="white")
msg.grid(row=5, column=2)

# Update message
def updateMessage(x):
    msg['text'] = x

# Update user score
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore["text"] = str(score)

# Update computer score
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore["text"] = str(score)

# Check winner
def checkWinner(player, computer):
    if player == computer:
        updateMessage("It's a Tie")

    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose")
            updateCompScore()
        elif computer == "scissor":
            updateMessage("You Won")
            updateUserScore()

    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose")
            updateCompScore()
        elif computer == "rock":
            updateMessage("You Won")
            updateUserScore()

    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose")
            updateCompScore()
        elif computer == "paper":
            updateMessage("You Won")
            updateUserScore()

    else:
        pass

# Update choices
choices = ["rock", "paper", "scissor"]
def updateChoice(x):

    # For computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        computer_label.configure(image=rock_computer)
    elif compChoice == "paper":
        computer_label.configure(image=paper_computer)
    elif compChoice == "scissor":
        computer_label.configure(image=scissor_computer)

    # For user
    if x == "rock":
        user_label.configure(image=rock_user)
    elif x == "paper":
        user_label.configure(image=paper_user)
    elif x == "scissor":
        user_label.configure(image=scissor_user)

    checkWinner(x, compChoice)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#0000ff", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#ff0000", fg="white", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#ff0066", fg="white", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3)

root.mainloop()
