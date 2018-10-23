import itertools

COORDS = "123456789"

class Sudoku:

    """
    INITIALIZATION 
    """
    def __init__(self, grid):

        # generation of all the coords of the grid
        self.cells = self.generate_coords()

        # generation of all the possibilities for each one of these coords
        self.possibilities = self.generate_possibilities(grid)

        # generation of the line / row / square constraints
        rule_constraints = self.generate_rules_constraints()

        # convertion of these constraints to binary constraints
        self.binary_constraints = self.generate_binary_constraints(rule_constraints)

        self.isFinished()

    """
    generates all the coordinates of the cells
    """
    def generate_coords(self):

        all_cells_coords = []

        for a in COORDS:

            for b in COORDS:
                new_coords = a + b
                all_cells_coords.append(new_coords)
        
        return all_cells_coords

    """
    generates all possible value remaining for each cell
    """
    def generate_possibilities(self, grid):

        grid_as_list = list(grid)

        possibilities = dict()
        default_possibilities = list(range(1,10))

        for index, coords in enumerate(self.cells):

            # if value is 0, then the cell can have any value in [1, 9]
            if grid_as_list[index] == "0":
                possibilities[coords] = default_possibilities
            # else value is already defined, possibilities is this value
            else:
                possibilities[coords] = [int(grid_as_list[index])]

        return possibilities

    """
    generates the constraints based on the rules of the game:
    value different from any in row, column or square
    """
    def generate_rules_constraints(self):
        column_constraints = []
        row_constraints = []
        square_constraints = []

        for row in COORDS:
            column_constraints.append([col + row for col in COORDS])

        for col in COORDS:
            row_constraints.append([col + row for row in COORDS])

        # get square constraints
        # how to split coords (non static): 
        # https://stackoverflow.com/questions/9475241/split-string-every-nth-character
        square_coords = (COORDS[i:i+3] for i in range(0, len(COORDS), 3))
        square_coords = list(square_coords)

        # for each square
        for row in square_coords:
            for col in square_coords:

                # and for each value in this square
                current_square_constraints = []
                for x in row:
                    for y in col:
                        current_square_constraints.append(x + y)
                square_constraints.append(current_square_constraints)

        return row_constraints + column_constraints + square_constraints

    """
    generates the binary constraints based on the rule constraints
    """
    def generate_binary_constraints(self, rule_constraints):
        generated_binary_constraints = list()

        # for each set of constraints
        for constraint_set in rule_constraints:

            binary_constraints = list()

            # 2 because we want binary constraints
            # solution taken from :
            # https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
            
            #for tuple_of_constraint in itertools.combinations(constraint_set, 2):
            for tuple_of_constraint in itertools.permutations(constraint_set, 2):
                binary_constraints.append(tuple_of_constraint)

            # for each of these binary constraints
            for constraint in binary_constraints:

                # check if we already have this constraint saved
                # = check if already exists
                # solution from https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list
                constraint_as_list = list(constraint)
                if(constraint_as_list not in generated_binary_constraints):
                    generated_binary_constraints.append([constraint[0], constraint[1]])

        return generated_binary_constraints

    """
    checks if the Sudoku's solution is finished
    we loop through the possibilities for each cell
    if all of them has only one, then the Sudoku is solved
    """
    def isFinished(self):

        for coords, possibilities in self.possibilities.items():
            if len(possibilities) > 1:
                return False
        
        return True
