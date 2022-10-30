class Cell:
    def __init__(self, x, y, visited, occupant):
        self.x = x
        self.y = y
        self.occupant = occupant
        self.visited = visited