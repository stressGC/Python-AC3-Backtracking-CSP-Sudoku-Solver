import argparse
import sys
from sudoku import Sudoku
from ac3 import AC3
from backtrack import recursive_backtrack_algorithm

"""
default sudokus' grid
"""
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
    
    sudoku_grid_as_string = "000079065000003002005060093340050106000000000608020059950010600700600000820390000"
    sudoku = Sudoku(sudoku_grid_as_string)

    AC3_result = AC3(sudoku)

    if not AC3_result:
        print("Sudoku has no solution")

    else:

        if sudoku.isFinished():
            print("AC3 was enough to solve this sudoku!")

        else:
            print("AC3 finished, backtracking starting...")

            assignment = {}

            for x in sudoku.cells:
                if len(sudoku.possibilities[x]) == 1:
                    assignment[x] = sudoku.possibilities[x][0]
            
            assignment = recursive_backtrack_algorithm(assignment, sudoku)
            
            for d in sudoku.possibilities:
                sudoku.possibilities[d] = assignment[d] if len(d) > 1 else sudoku.possibilities[d]
            
            if assignment:
                print("Result : ")
                print(sudoku)

            else:
                print("No solution exists")
    