coords = "123456789"

class Sudoku:

    def __init__(self, board):
        self.generate_coords()


    def generate_coords(self):
        all_cells_coords = []
        for a in coords:
            for b in coords:
                new_coords = a + b
                all_cells_coords.append(new_coords)
        
        self.cells = all_cells_coords

sudoku = Sudoku("aeeee")
