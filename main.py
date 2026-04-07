# tic-tac-toe/main.py
# We use a simple list of strings to represent the 9 squares of the tic-tac-toe board. Initially, they are all empty.
board = [" " for _ in range(9)]
current_player = "X"
game_over = False
turns_played = 0

print("Welcome to Terminal Tic-Tac-Toe!")

# The main game loop will be displayed here.
while not game_over:
	
    print("\n      KEY          GAME BOARD")
    print(f"  1 | 2 | 3      {board[0]} | {board[1]} | {board[2]}")
    print(f" ---|---|---    ---|---|---")
    print(f"  4 | 5 | 6      {board[3]} | {board[4]} | {board[5]}")
    print(f" ---|---|---    ---|---|---")
    print(f"  7 | 8 | 9      {board[6]} | {board[7]} | {board[8]}")

    # This is where we will handle the player's input and update the game as we go.

    move = input(f"\nPlayer {current_player}, enter your move (1-9): ")

    if move.isdigit() and 1 <= int (move) <= 9:
        index = int(move) - 1
        if board[index] != "X" and board[index] != "O":
            board[index] = current_player
            turns_played += 1
        else:
             print("That square is already taken. Please choose another one.")
    else:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    # Here we will check for a win or a draw after each move.

    win_found = False

    # Here, we will check all the winning combinations (horizontal, vertical, diagonal) to see if the current player has won.
    # Horizontal wins

    if board[0] == board[1] == board[2] != " ":
        win_found = True
    elif board[3] == board[4] == board[5] != " ":
        win_found = True
    elif board[6] == board[7] == board[8] != " ":
        win_found = True
    # Vertical wins
    elif board[0] == board[3] == board[6] != " ":
        win_found = True
    elif board[1] == board[4] == board[7] != " ":
        win_found = True
    elif board[2] == board[5] == board[8] != " ":
        win_found = True
    # Diagonal wins
    elif board[0] == board[4] == board[8] != " ":
        win_found = True
    elif board[2] == board[4] == board[6] != " ":
        win_found = True
    
    if win_found:
        # Print the final winning board.
        print("\n      KEY          GAME BOARD")
        print(f"  1 | 2 | 3      {board[0]} | {board[1]} | {board[2]}")
        print(f" ---|---|---    ---|---|---")
        print(f"  4 | 5 | 6      {board[3]} | {board[4]} | {board[5]}")
        print(f" ---|---|---    ---|---|---")
        print(f"  7 | 8 | 9      {board[6]} | {board[7]} | {board[8]}")
        print(f"\nCongratulations, Player {current_player}! You win!") 
        game_over = True
        break 

    def change_player():
        print(f"Player {current_player} has made their move.")

if __name__ == "__main__":
	# The pass is there so the terminal does not throw an error.
	pass
    