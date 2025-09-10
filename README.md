# Command-Line Battleship: Player vs. AI
This is a classic game of Battleship recreated in Python, running directly in your terminal. This project features a clean, user-friendly command-line interface where the player competes against a randomized computer opponent.

## Key Features
Player vs. Computer: Engage in a full game against a computer AI that makes random, non-repeating shots.

Dynamic Board Setup: The user can customize the size of the game board and the number of ships at the start of each game.

Robust Input Validation: The application is built to handle invalid user inputs gracefully, preventing crashes from non-numeric or out-of-bounds entries.

Clear UI: The game boards are displayed with clear row and column headers, making it easy to track shots and plan your next move.

Modular Codebase: The logic is separated into distinct, well-documented functions for creating the board, placing ships, processing shots, and managing game flow.

## How to Play
The objective is to sink all of the computer's ships before it sinks all of yours.

1. At the start, you will define the board size and the number of ships.

2. Ships are placed randomly on both your board and the computer's board.

3. On your turn, you will see your board (with your ships visible) and the computer's board (where their ships are hidden).

4. Enter coordinates (e.g., 3 1 for row 3, column 1) to fire a shot at the computer's board.
    - X marks a hit.
    - O marks a miss.

5. The computer will then take its turn, firing at your board.

6. The game continues until one player has no ships remaining.

## Prerequisites
Make sure you have Python 3 installed on your system.

## Installation
1. On the main GitHub repository page, click the green <> Code button.

2. Select Download ZIP.

3. Extract the contents of the ZIP file to a location on your computer.

4. Open your terminal and navigate into the extracted folder.

## Running the Game
Run the main application file from your terminal. No external libraries are needed.
```
python battleShip.py
```
## Example Gameplay
```
--- Welcome to Battleship! ---
Enter the size of the board (e.g., 5 for a 5x5 board): 5
Enter the number of ships (1 to 8): 5

--- YOUR TURN ---
Your Board:
  0 1 2 3 4
0 ~ ~ ~ ~ ~
1 S ~ ~ ~ ~
2 ~ ~ S ~ ~
3 ~ S ~ S ~
4 ~ ~ ~ ~ S

Computer's Board:
  0 1 2 3 4
0 ~ ~ ~ ~ ~
1 ~ ~ ~ ~ ~
2 ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~
4 ~ ~ ~ ~ ~
Enter coordinates for your shot (e.g., 3 1): 2 2

IT'S A HIT!

--- COMPUTER'S TURN ---
The computer fires at (3, 1)...
YOUR SHIP WAS HIT!

Ships remaining -> You: 4 | Computer: 4
Press Enter to continue to the next turn...
```
