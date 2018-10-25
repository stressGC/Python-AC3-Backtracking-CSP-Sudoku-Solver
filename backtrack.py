from heuristics import select_unassigned_variable, order_domain_values
from utils import is_consistent, assign, unassign

"""
Backtracking Algorithm
pseudo code found @ https://sandipanweb.files.wordpress.com/2017/03/im31.png
"""
def recursive_backtrack_algorithm(assignment, sudoku):

    # if assignment is complete then return assignment
    if len(assignment) == len(sudoku.cells):
        return assignment

    # var = select-unassigned-variables(csp)
    cell = select_unassigned_variable(assignment, sudoku)

    # for each value in order-domain-values(csp, var)
    for value in order_domain_values(sudoku, cell):

        # if value is consistent with assignment
        if is_consistent(sudoku, assignment, cell, value):

            # add {cell = value} to assignment
            assign(sudoku, cell, value, assignment)

            # result = backtrack(assignment, csp)
            result = recursive_backtrack_algorithm(assignment, sudoku)

            # if result is not a failure return result
            if result:
                return result

            # remove {cell = value} from assignment
            unassign(sudoku, cell, assignment)
   
    # return failure
    return False