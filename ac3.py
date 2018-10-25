from utils import is_different

"""
Constraint Propagation with AC-3
pseudo code found @ https://en.wikipedia.org/wiki/AC-3_algorithm
python implementation inspired by http://aima.cs.berkeley.edu/python/csp.html
"""
def AC3(csp, queue=None):

    if queue == None:
        queue = list(csp.binary_constraints)

    while queue:

        (xi, xj) = queue.pop(0)

        if remove_inconsistent_values(csp, xi, xj): 

            # if a cell has 0 possibilities, sudoku has no solution
            if len(csp.possibilities[xi]) == 0:
                return False
            
            for Xk in csp.related_cells[xi]:
                if Xk != xi:
                    queue.append((Xk, xi))
                    
    return True

"""
remove_inconsistent_values

returns true if a value is removed
"""
def remove_inconsistent_values(csp, cell_i, cell_j):

    removed = False

    # for each possible value remaining for the cell_i cell
    for value in csp.possibilities[cell_i]:

        # if cell_i=value is in conflict with cell_j=poss for each possibility
        if not any([is_different(value, poss) for poss in csp.possibilities[cell_j]]):
            
            # then remove cell_i=value
            csp.possibilities[cell_i].remove(value)
            removed = True

    # returns true if a value has been removed
    return removed
