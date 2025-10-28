import random
from environment import GRID_SIZE

class Agent:
    def __init__(self, env):
        self.env = env
        self.pos = env.agent_pos
        self.safe = {tuple(self.pos)}
        self.visited = {tuple(self.pos)}
        self.knowledge = {}
        self.found_gold = False

    def get_possible_moves(self):
        x, y = self.pos
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        valid = []
        for dx, dy in moves:
            if 0 <= x+dx < GRID_SIZE and 0 <= y+dy < GRID_SIZE:
                valid.append([x+dx, y+dy])
        return valid

    def perceive_and_update(self):
        percepts = self.env.get_percepts(self.pos)
        self.knowledge[tuple(self.pos)] = percepts

        if "glitter" in percepts:
            self.found_gold = True
            print("🏆 Gold found at", self.pos)

        adj = self.env.adjacent_cells(self.pos)

        if not percepts:
            for cell in adj:
                self.safe.add(tuple(cell))
        else:
            if "breeze" in percepts or "stench" in percepts:
                pass  # uncertain cells remain unknown
        return percepts

    def choose_next_move(self):
        adj = self.env.adjacent_cells(self.pos)
        for cell in adj:
            if tuple(cell) in self.safe and tuple(cell) not in self.visited:
                return cell
        for cell in adj:
            if tuple(cell) not in self.visited:
                return cell
        return random.choice(adj)
