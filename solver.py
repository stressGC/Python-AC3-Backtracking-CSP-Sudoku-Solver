import argparse
import sys
from sudoku import Sudoku

sudokus = dict(
    easy = "000079065000003002005060093340050106000000000608020059950010600700600000820390000",
    medium = "102004070000902800009003004000240006000107000400068000200800700007501000080400109",
    hard = "002008050000040070480072000008000031600080005570000600000960048090020000030800900"
    )

def ac3(sudoku):

    queue = list(sudoku.binary_constraints)

    while queue:

        xi, xj = queue.pop(0)

        if revise(sudoku, xi, xj):

            if len(sudoku.possibilities[xi]) == 0:
                return False

            for xk in sudoku.related_cells[xi]:
                if xk != xi:
                    queue.append([xk, xi])

    return True

@staticmethod
def constraint(xi, xj): return xi != xj

def revise(sudoku, xi, xj):

    revised = False

    for x in sudoku.possibilities[xi]:
        if not any([sudoku.constraint(x, y) for y in sudoku.possibilities[xj]]):
            sudoku.possibilities[xi].remove(x)
            revised = True
        
    return revised

# def AC3(csp, queue=None):

#     if queue == None:
#         queue = list(sudoku.binary_constraints)
#     while queue:
#         (Xi, Xj) = queue.pop()
#         if remove_inconsistent_values(csp, Xi, Xj):
#             for Xk in csp.related_cells[Xi]:
#                 queue.append((Xk, Xi))

# def remove_inconsistent_values(csp, Xi, Xj):
#     "Return true if we remove a value."
#     removed = False
#     for x in csp.possibilities[Xi][:]:
#         # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
#         # if every(lambda y: not csp.binary_constraints(Xi, x, Xj, y), csp.possibilities[Xj]):
#         if not any([csp.constraint(x, y) for y in csp.possibilities[Xj]]):
#             csp.possibilities[Xi].remove(x)
#             removed = True 

#     return removed


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


    result = ac3(sudoku)
    for i, x in enumerate(sudoku.possibilities):
        print(i, x, sudoku.possibilities[x])
    print(result)