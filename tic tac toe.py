from tkinter import *
import random

def next_turn(row, column):
    """
    Handles the logic for the next turn in the game.

    Parameters:
    - row (int): The row index of the button clicked.
    - column (int): The column index of the button clicked.
    """
    global player

    # Check if the clicked button is empty and there is no winner yet
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # If the current player is the first player
        if player == players[0]:
            buttons[row][column]['text'] = player

            # Check if there is a winner or if it's a tie
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        else:
            # If the current player is the second player
            buttons[row][column]['text'] = player

            # Check if there is a winner or if it's a tie
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():
    """
    Checks if there is a winner or a tie in the game.

    Returns:
    - True if there is a winner.
    - "Tie" if the game is a tie.
    - False if the game is still ongoing.
    """
    # Check rows for a winner
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # Check columns for a winner
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Check diagonals for a winner
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        # If there are no empty spaces, it's a tie
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False

def empty_spaces():
    """
    Checks if there are any empty spaces left on the grid.

    Returns:
    - False if there are no empty spaces (tie).
    - True if there are still empty spaces.
    """
    spaces = 9

    # Count the number of empty spaces on the grid
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    """
    Resets the game to its initial state.
    """
    global player

    # Randomly select a player to start the new game
    player = random.choice(players)

    # Update the label to display the starting player's turn
    label.config(text=player + " turn")

    # Reset all buttons to be empty and set their background color to default
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Create the main window
window = Tk()
window.title("Tic-Tac-Toe")

# Define the players
players = ["x", "o"]
player = random.choice(players)

# Create a 3x3 grid to hold the button widgets
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Create a label to display the current player's turn or the result of the game
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

# Create a button to restart the game
reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Create a frame to hold the grid of buttons
frame = Frame(window)
frame.pack()

# Create and place the 3x3 grid of buttons inside the frame
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the Tkinter event loop to run the application
window.mainloop()
