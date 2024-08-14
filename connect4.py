import tkinter as tk
from tkinter import messagebox

click_count = 0
clicked_buttons = set()

def change_color(button, row, col):
    global click_count, clicked_buttons
    if row == 5 or (row + 1, col) in clicked_buttons:
        if click_count % 2 == 0:
            button.config(bg='blue', state='disabled')  # Disable button after click
            button.color = 'blue'
        else:
            button.config(bg='red', state='disabled')   # Disable button after click
            button.color = 'red'
        clicked_buttons.add((row, col))
        click_count += 1
# to check for winner then end game
        if check_win(board):
            display_winner(button.color)
            disable_all_buttons()

def display_winner(color):
    messagebox.showinfo("Game Over", f"{color.capitalize()} wins!")

def disable_all_buttons():
    for row in board:
        for button in row:
            button.config(state='disabled')

def check_win(board):
    # Check rows
    for row in board:
        for i in range(len(row) - 3):
            if row[i].color == row[i+1].color == row[i+2].color == row[i+3].color and row[i].color != "":
                return True

    # Check columns
    for col in range(len(board[0])):
        for i in range(len(board) - 3):
            if board[i][col].color == board[i+1][col].color == board[i+2][col].color == board[i+3][col].color and board[i][col].color != "":
                return True

    # Check diagonals
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if board[i][j].color == board[i+1][j+1].color == board[i+2][j+2].color == board[i+3][j+3].color and board[i][j].color != "":
                return True
            if board[i][j+3].color == board[i+1][j+2].color == board[i+2][j+1].color == board[i+3][j].color and board[i][j+3].color != "":
                return True

    return False

def create_grid(window, rows, columns):
    board = [[None for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            button = tk.Button(master=frame, text="Connect \n 4", bg='white') # replace text with {f"Row {i}\nColumn {j}"} for row and column name
            button.color = ""
            button.config(command=lambda b=button, r=i, c=j: change_color(b, r, c))
            button.pack()
            board[i][j] = button
    return board



window = tk.Tk()
window.title("CONNECT 4-ELVIS")
board = create_grid(window, 6, 7)

window.mainloop()
