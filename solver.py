import argparse
import sys
from sudoku import Sudoku

sudokus = dict(
    easy = "000079065000003002005060093340050106000000000608020059950010600700600000820390000",
    medium = "102004070000902800009003004000240006000107000400068000200800700007501000080400109",
    hard = "002008050000040070480072000008000031600080005570000600000960048090020000030800900"
    )

if __name__ == "__main__":
    # argument parsing using argparse module
    # doc @ https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='Solve a Sudoku with CSP')
    parser.add_argument('--string', type=str, help='Sudoku as String')

    args = parser.parse_args()

    sudoku_grid_as_string = args.string
    

    if sudoku_grid_as_string is None or len(sudoku_grid_as_string) != 81:
        sudoku_grid_as_string = sudokus["easy"]
    
    sudoku = Sudoku(sudoku_grid_as_string)


