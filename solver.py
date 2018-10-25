import argparse
import sys

from sudoku import Sudoku
from utils import is_different 

sudokus = dict(
    easy = "000079065000003002005060093340050106000000000608020059950010600700600000820390000",
    medium = "102004070000902800009003004000240006000107000400068000200800700007501000080400109",
    hard = "002008050000040070480072000008000031600080005570000600000960048090020000030800900"
    )

"""
Constraint Propagation with AC-3
pseudo code found @ https://en.wikipedia.org/wiki/AC-3_algorithm
python implementation inspired by http://aima.cs.berkeley.edu/python/csp.html
"""
def AC3(csp, queue=None):

    if queue == None:
        queue = list(sudoku.binary_constraints)

    while queue:

        (xi, xj) = queue.pop()

        if remove_inconsistent_values(csp, xi, xj):

            # check if the 
            if len(csp.possibilities[xi]) == 0:
                return False

            for Xk in csp.related_cells[xi]:
                queue.append((Xk, xi))

    return True

"""
Remove inconsistent values
returns true if a value is removed
"""
def remove_inconsistent_values(csp, xi, xj):
    removed = False

    for x in csp.possibilities[xi][:]:
        # If xi=x conflicts with xj=y for every possible y, eliminate xi=x
        # if every(lambda y: not csp.binary_constraints(xi, x, xj, y), csp.possibilities[xj]):
        if not any([is_different(x, y) for y in csp.possibilities[xj]]):
            csp.possibilities[xi].remove(x)
            removed = True 

    return removed


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

    # sudoku has no solution
    if not AC3_result:
        print("The sudoku has no solution")
    
    else:
        for i, x in enumerate(sudoku.possibilities):
            print(x, ",", sudoku.possibilities[x])