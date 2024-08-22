Sudoku Game

Overview

This project implements a Sudoku game using Pygame. The game features a grid where players can input numbers to complete the Sudoku puzzle. The game validates the inputs and provides visual feedback for valid and invalid entries.

Features

 • Sudoku Grid: A 9x9 grid representing the Sudoku puzzle.
 • Number Input: Players can input numbers between 1 and 9.
 • Validation: The game checks if the input number is valid based on Sudoku rules.
 • Visual Feedback: Valid inputs are highlighted in green, and invalid inputs are highlighted in red.
 • Random Puzzle Generation: The game generates a random Sudoku puzzle with some cells pre-filled.

Installation

 1. Install Pygame: Make sure you have Pygame installed. If not, you can install it using pip:

pip install pygame


 3. Run the Game: Navigate to the project directory and run the script:

python sudoku.py


Usage

 • Input Numbers: Click on a cell and press a number key (1-9) to input a number into that cell.
 • Clear Cell: Press the ‘0’ key to clear the cell.

Code Description

 • generate_board(): Creates a new Sudoku board with a mix of pre-filled and empty cells.
 • is_valid(board, num, pos): Checks if placing a number in a specified position is valid according to Sudoku rules.
 • draw_grid(win, board): Draws the Sudoku grid and fills in the numbers.
 • insert_num(win, board, position): Handles user input and updates the board.

Customization

 • Grid Colors: Modify the WHITE, BLACK, GREY, RED, YELLOW, PINK, and GREEN color values to customize the appearance of the grid and feedback.
 • Font Sizes: Adjust the font and small_font sizes to change the text appearance.

Contributing

If you’d like to contribute to this project, please fork the repository and submit a pull request with your changes.