from tkinter import *
from tkinter import messagebox
import os
import random

# Get the current working directory
cwd = os.getcwd()

# Main window
root = Tk()
root.title("Tic Tac Toe Game")
root.configure(background="black")

# Function to check winner
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

# Function to check if the board is full
def check_board_full(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

# Function to handle button click
def on_button_click(row, col):
    global board, winner

    if board[row][col] == "" and winner is None:
        buttons[row][col]["text"] = "X"
        board[row][col] = "X"
        buttons[row][col].config(bg="green")

        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
            return

        if check_board_full(board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
            return

        computer_turn(board)

# Function for computer's turn
def computer_turn(board):
    global winner

    # Medium-level AI: try to win or block player from winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                if check_winner(board) == "O":
                    buttons[i][j]["text"] = "O"
                    buttons[i][j].config(bg="red")
                    winner = "O"
                    if winner:
                        messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                        reset_game()
                        return
                    return
                else:
                    board[i][j] = ""
    
    # Block player's potential win
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                if check_winner(board) == "X":
                    buttons[i][j]["text"] = "O"
                    buttons[i][j].config(bg="red")
                    board[i][j] = "O"
                    return
                else:
                    board[i][j] = ""

    # Random move
    if winner is None:
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == "":
                buttons[row][col]["text"] = "O"
                board[row][col] = "O"
                buttons[row][col].config(bg="red")
                
                winner = check_winner(board)
                if winner:
                    messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                    reset_game()
                    return
                break

        if check_board_full(board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_game()
            return

# Function to reset the game
def reset_game():
    global board, winner
    winner = None
    board = [["" for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j].config(bg="SystemButtonFace")

# Initialize variables
board = [["" for _ in range(3)] for _ in range(3)]
winner = None

# Buttons
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = Button(root, text="", font=("Helvetica", 20), bg="SystemButtonFace", fg="white", width=10, height=3, command=lambda r=i, c=j: on_button_click(r, c))
        btn.grid(row=i+1, column=j, padx=10, pady=10)
        row.append(btn)
    buttons.append(row)

# Reset button
reset_btn = Button(root, text="Reset", font=("Helvetica", 16), bg="grey", fg="white", width=20, command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
