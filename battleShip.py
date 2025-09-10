import random
import time

def create_board(size: int) -> list[list[str]]:
    """Creates a square game board of a given size.

    This uses a list comprehension for a concise, Pythonic implementation.

    Args:
        size: The integer size of the board (e.g., 5 for a 5x5 board).

    Returns:
        A list of lists representing the board, initialized with '~' (water).
    """
    return [['~' for _ in range(size)] for _ in range(size)]

def place_ships(board: list[list[str]], num_ships: int):
    """Randomly places a given number of single-cell ships ('S') on the board.

    Args:
        board: The game board (list of lists).
        num_ships: The number of ships to place.
    """
    size = len(board)
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] == '~':
            board[row][col] = 'S'
            ships_placed += 1

def display_board(board: list[list[str]], hide_ships: bool = False):
    """Displays the current state of the board with headers.

    Args:
        board: The game board to display.
        hide_ships: If True, 'S' will be displayed as '~'. Used for showing
                    the opponent's board to the player.
    """
    size = len(board)
    # Print column headers
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        display_row = []
        for cell in row:
            if hide_ships and cell == 'S':
                display_row.append('~')
            else:
                display_row.append(cell)
        # Print row header and the row itself
        print(f"{i} " + " ".join(display_row))

def get_player_shot(size: int) -> tuple[int, int]:
    """Gets and validates shot coordinates from the player.

    This function includes error handling to prevent crashes from bad input.

    Args:
        size: The size of the board, used for input validation.

    Returns:
        A tuple containing the valid (row, col) coordinates.
    """
    while True:
        try:
            shot_input = input(f"Enter coordinates for your shot (e.g., 3 1): ").split()
            if len(shot_input) != 2:
                print("Error: Please enter exactly two numbers separated by a space.")
                continue
            row = int(shot_input[0])
            col = int(shot_input[1])
            if not (0 <= row < size and 0 <= col < size):
                print("Error: Coordinates are out of bounds.")
                continue
            return row, col
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")

def process_shot(board: list[list[str]], row: int, col: int) -> bool:
    """Processes a shot on the board and updates its state.

    Args:
        board: The board being fired upon.
        row: The row coordinate of the shot.
        col: The column coordinate of the shot.

    Returns:
        True if the shot was a hit, False otherwise.
    """
    if board[row][col] == 'S':
        board[row][col] = 'X'  # Hit
        return True
    elif board[row][col] == '~':
        board[row][col] = 'O'  # Miss
        return False
    else:
        # This spot has already been shot ('X' or 'O')
        return False

def computer_turn(player_board: list[list[str]], previous_guesses: set) -> tuple[int, int]:
    """Generates a non-repeating random shot for the computer.

    Args:
        player_board: The player's board (used for size).
        previous_guesses: A set of (row, col) tuples of the computer's past shots.

    Returns:
        The (row, col) coordinates of the computer's shot.
    """
    size = len(player_board)
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in previous_guesses:
            previous_guesses.add((row, col))
            return row, col

def main():
    """Main function to run the Battleship game."""
    print("--- Welcome to Battleship! ---")
    
    # Game Setup
    while True:
        try:
            size = int(input("Enter the size of the board (e.g., 5 for a 5x5 board): "))
            if size < 3 or size > 10:
                print("Please choose a size between 3 and 10.")
                continue
            
            max_ships = size * size // 3
            num_ships = int(input(f"Enter the number of ships (1 to {max_ships}): "))
            if 1 <= num_ships <= max_ships:
                break
            else:
                print(f"Invalid number of ships. Please choose between 1 and {max_ships}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create boards and place ships
    player_board = create_board(size)
    computer_board = create_board(size)
    
    place_ships(player_board, num_ships)
    place_ships(computer_board, num_ships)
    
    player_ships_remaining = num_ships
    computer_ships_remaining = num_ships
    computer_guesses = set()

    # Main Game Loop 
    while player_ships_remaining > 0 and computer_ships_remaining > 0:
        # Player's Turn 
        print("\n--- YOUR TURN ---")
        print("Your Board:")
        display_board(player_board)
        print("\nComputer's Board:")
        display_board(computer_board, hide_ships=True)
        
        while True:
            row, col = get_player_shot(size)
            if computer_board[row][col] in ('X', 'O'):
                print("You've already shot there. Try again.")
            else:
                break
        
        if process_shot(computer_board, row, col):
            print("\nIT'S A HIT!")
            computer_ships_remaining -= 1
        else:
            print("\nYOU MISSED!")
        
        if computer_ships_remaining == 0:
            break

        # Computer's Turn 
        print("\n--- COMPUTER'S TURN ---")
        time.sleep(1) 
        comp_row, comp_col = computer_turn(player_board, computer_guesses)
        print(f"The computer fires at ({comp_row}, {comp_col})...")
        time.sleep(1)

        if process_shot(player_board, comp_row, comp_col):
            print("YOUR SHIP WAS HIT!")
            player_ships_remaining -= 1
        else:
            print("THEY MISSED!")
            
        print(f"\nShips remaining -> You: {player_ships_remaining} | Computer: {computer_ships_remaining}")
        input("Press Enter to continue to the next turn...")

    # End of Game 
    print("\n--- GAME OVER ---")
    print("Your final board:")
    display_board(player_board)
    print("\nComputer's final board:")
    display_board(computer_board)

    if player_ships_remaining == 0:
        print("\nThe computer has sunk all your ships! You lose.")
    else:
        print("\nYou have sunk all the computer's ships! YOU WIN!")

if __name__ == '__main__':
    main()

