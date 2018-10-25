from utils import number_of_conflicts

"""
Most Constrained Variable (MRV) heuristic

definitions & explanations @ https://www.cs.unc.edu/~lazebnik/fall10/lec08_csp2.pdf
returns the variable with the fewest possible values remaining
"""
def select_unassigned_variable(assignment, sudoku):

    unassigned = []

    # for each of the cells
    for cell in sudoku.cells:

        # if the cell is not in the assignment
        if cell not in assignment:

            # add it
            unassigned.append(cell)

    # the criterion here is the length of the possibilities (MRV)
    criterion = lambda cell: len(sudoku.possibilities[cell])

    # we return the variable with the fewest possible values remaining
    return min(unassigned, key=criterion)

"""
Least Constraining Value (LCV) heuristic

@ https://cs.stackexchange.com/questions/47870/what-is-least-constraining-value
from "Artificial Intelligence: A Modern Approach (Russel & Norvig)"'s definition:
prefers the value that rules out the fewest choices for the neighboring variables in the constraint graph.
"""
def order_domain_values(sudoku, cell):

    # since we are looking for the least constraining value
    # contained in [1, 2, 3, ..., 8, 9], smallest case possible is length of 1
    if len(sudoku.possibilities[cell]) == 1:
        return sudoku.possibilities[cell]

    # we want to sort based on the number of conflicts
    criterion = lambda value: number_of_conflicts(sudoku, cell, value)
    return sorted(sudoku.possibilities[cell], key=criterion)