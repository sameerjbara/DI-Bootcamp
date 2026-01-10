# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.



# Step 1: Representing the Game Board

# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).


# Step 2: Displaying the Game Board

# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.


# Step 3: Getting Player Input

# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.


# Step 4: Checking for a Winner

# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.


# Step 5: Checking for a Tie

# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.


# Step 6: The Main Game Loop

# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).


# Tips:

# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.


# Tic Tac Toe (3x3) — console version

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\nTIC TAC TOE")
    print("*" * 19)
    for r in range(3):
        row = f"*  {board[r][0]} | {board[r][1]} | {board[r][2]}  *"
        print(row)
        if r < 2:
            print("* ---|---|--- *")
    print("*" * 19)
    print()

def player_input(board, player):
    while True:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
        except ValueError:
            print("Please enter numbers only (0, 1, or 2).\n")
            continue

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Row/Column must be 0, 1, or 2.\n")
            continue

        if board[row][col] != " ":
            print("That spot is already taken. Choose another.\n")
            continue

        return row, col

def check_win(board, player):
    # rows
    for r in range(3):
        if all(board[r][c] == player for c in range(3)):
            return True

    # columns
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True

    # diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_tie(board):
    # tie means: no empty spaces left
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True

def switch_player(player):
    return "O" if player == "X" else "X"

def play():
    print("Welcome to TIC TAC TOE!")
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        print(f"Player '{current_player}'s turn...\n")

        row, col = player_input(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player '{current_player}' wins!")
            break

        if is_tie(board):
            display_board(board)
            print("🤝 It's a tie!")
            break

        current_player = switch_player(current_player)

if __name__ == "__main__":
    play()
