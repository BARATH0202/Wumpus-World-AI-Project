import random

GRID_SIZE = 4

class Environment:
    def __init__(self):
        self.gold = self.random_cell([])
        self.wumpus = self.random_cell([self.gold])
        self.pits = [self.random_cell([self.gold, self.wumpus]) for _ in range(3)]
        self.agent_pos = [0, 0]

    def random_cell(self, exclude):
        while True:
            pos = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
            if pos not in exclude:
                return pos

    def get_percepts(self, pos):
        """Return percepts based on adjacent cells"""
        percepts = []
        adj = self.adjacent_cells(pos)
        if any(p in adj for p in self.pits):
            percepts.append("breeze")
        if any(p == self.wumpus for p in adj):
            percepts.append("stench")
        if pos == self.gold:
            percepts.append("glitter")
        return percepts

    def adjacent_cells(self, pos):
        x, y = pos
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        valid = []
        for dx, dy in moves:
            if 0 <= x+dx < GRID_SIZE and 0 <= y+dy < GRID_SIZE:
                valid.append([x+dx, y+dy])
        return valid
