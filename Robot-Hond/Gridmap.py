import Cell

class Gridmap:
    def __init__(self, width, height, resolution):
        self.width = width
        self.heigth = height
        self.resolution = resolution
        self.grid = []
        self.grid_row = int(width/resolution)
        self.grid_collum = int(height/resolution)
        self.polulate_grid()
        self.last_cell = self.grid[self.grid_row - 1][self.grid_collum - 1]

    def polulate_grid(self):
        for x in range(self.grid_row):
            self.grid.append([])
            for y in range(self.grid_collum):
                # Elke Cell wordt aangemaakt met (x,y) en gevlagd als niet bezocht en niet bezet.
                newCell = Cell.Cell(x, y, False, False)
                self.grid[x].append(newCell)


    def show_map(self):
        for x in range(self.grid_row):
            for y in range(self.grid_collum):
                print("Cell " + str((x,y)) + " " + str(self.grid[x][y].visited ) + " " + str(self.grid[x][y].occupant))


if __name__ == '__main__':
    pass