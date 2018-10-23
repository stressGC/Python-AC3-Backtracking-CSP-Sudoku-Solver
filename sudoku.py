import numpy as np

COORDS = "123456789"

class Sudoku:

    """
    INITIALIZATION 
    """
    def __init__(self, grid):

        self.cells = self.generate_coords()

        self.possibilities = self.generate_possibilities(grid)

        rule_constraints = self.generate_rules_constraints()
        self.binary_constraints = self.generate_binary_constraints(rule_constraints)

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
        print(rule_constraints)





grid = "000079065000003002005060093340050106000000000608020059950010600700600000820390000"
sudoku = Sudoku(grid)

# easy 000079065000003002005060093340050106000000000608020059950010600700600000820390000
# medium 102004070000902800009003004000240006000107000400068000200800700007501000080400109
# hard 002008050000040070480072000008000031600080005570000600000960048090020000030800900 