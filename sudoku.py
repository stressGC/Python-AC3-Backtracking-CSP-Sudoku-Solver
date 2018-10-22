import numpy as np

COORDS = "123456789"

class Sudoku:

    """
    INITIALIZATION 
    """
    def __init__(self, grid):
        self.cells = self.generate_coords()
        self.possibilities = self.generate_possibilities(grid)


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

grid = "000079065000003002005060093340050106000000000608020059950010600700600000820390000"
sudoku = Sudoku(grid)
