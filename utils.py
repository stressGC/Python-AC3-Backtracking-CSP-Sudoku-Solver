import sys

def is_different(xi, xj):
    result = xi != xj
    return result

"""
number of conflicts
counts the number of conflicts for a cell with a specific value
"""
def number_of_conflicts(sudoku, cell, value):

    count = 0

    # for each of the cells that can be in conflict with cell
    for related_c in sudoku.related_cells[cell]:

        # if the value of related_c is not found yet AND the value we look for exists in its possibilities
        if len(sudoku.possibilities[related_c]) > 1 and value in sudoku.possibilities[related_c]:
            
            # then a conflict exists
            count += 1

    return count

"""
is_consistent

checks if the value is consistent in the assignments
"""
def is_consistent(sudoku, assignment, cell, value):

    is_consistent = True

    # for each tuple of cell/value in assignment
    for current_cell, current_value in assignment.items():

        # if the values are the equal and the cells are related to each other
        if current_value == value and current_cell in sudoku.related_cells[cell]:

            # then cell is not consistent
            is_consistent = False
    
    # else is it consistent
    return is_consistent

"""
assign
add {cell: val} to assignment
inspired by @ http://aima.cs.berkeley.edu/python/csp.html
"""
def assign(sudoku, cell, value, assignment):
    
    # add {cell: val} to assignment
    assignment[cell] = value

    if sudoku.possibilities:

        # forward check
        forward_check(sudoku, cell, value, assignment)

"""
unassign
remove {cell: val} from assignment (backtracking)
inspired by @ http://aima.cs.berkeley.edu/python/csp.html
"""
def unassign(sudoku, cell, assignment):

    # if the cell is in assignment
    if cell in assignment:

        # for coord, each value in pruned
        for (coord, value) in sudoku.pruned[cell]:

            # add it to the possibilities
            sudoku.possibilities[coord].append(value)

        # reset pruned for the cell
        sudoku.pruned[cell] = []

        # and delete its assignment
        del assignment[cell]

"""
forward check
domain reduction for the current assignment
idea based on @ https://github.com/ishpreet-singh/Sudoku
"""
def forward_check(sudoku, cell, value, assignment):

    # for each related cell of cell
    for related_c in sudoku.related_cells[cell]:

        # if this cell is not in assignment
        if related_c not in assignment:

            # and if the value remains in the possibilities
            if value in sudoku.possibilities[related_c]:

                # removed it from the possibilities
                sudoku.possibilities[related_c].remove(value)

                # and add it to pruned
                sudoku.pruned[cell].append((related_c, value))

"""
fetch sudokus
fetches sudokus based on user's input
"""
def fetch_sudokus(input):

        DEFAULT_SIZE = 81

        # if the input is an multiple of DEFAULT_SIZE=81
        if (len(input) % DEFAULT_SIZE) != 0:
                print("Error : the string must be a multiple of {}".format(DEFAULT_SIZE))
                sys.exit()
        
        else:
                formatted_input = input.replace("X", "0").replace("#", "0").replace("@", "0")

                if not formatted_input.isdigit():

                        print("Error : only the following characters are allowed: [1,9], 'X', '#' and '@'")
                        sys.exit()
                
                else:
                        return [formatted_input[i:i+DEFAULT_SIZE] for i in range(0, len(formatted_input), DEFAULT_SIZE)]
