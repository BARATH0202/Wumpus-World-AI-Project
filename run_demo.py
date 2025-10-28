import os
print("Current working directory:", os.getcwd())
import tkinter as tk
import time
from environment import Environment, GRID_SIZE
from agent import Agent

CELL_SIZE = 100

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Wumpus World AI Simulation 🧠")
        self.canvas = tk.Canvas(master, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, bg="#F8F6E7")
        self.canvas.pack()

        self.env = Environment()
        self.agent = Agent(self.env)

        self.draw_grid()
        self.draw_world()
        self.update_gui()

        self.master.after(1000, self.step)

    def draw_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    def draw_world(self):
        self.canvas.delete("all")
        self.draw_grid()
        # Pits
        for pit in self.env.pits:
            self.draw_emoji(pit, "🕳️")
        # Wumpus
        self.draw_emoji(self.env.wumpus, "👹")
        # Gold
        self.draw_emoji(self.env.gold, "💰")
        # Agent
        self.draw_emoji(self.agent.pos, "🤖")

    def draw_emoji(self, pos, emoji):
        x, y = pos[1]*CELL_SIZE + CELL_SIZE//2, pos[0]*CELL_SIZE + CELL_SIZE//2
        self.canvas.create_text(x, y, text=emoji, font=("Arial", 40))

    def step(self):
        if self.agent.found_gold:
            print("🎉 AI Agent completed the mission!")
            return

        percepts = self.agent.perceive_and_update()
        print(f"🤖 At {self.agent.pos} perceives {percepts}")

        next_pos = self.agent.choose_next_move()
        self.agent.visited.add(tuple(next_pos))
        self.agent.pos = next_pos

        if next_pos == self.env.wumpus:
            print("💀 The agent was eaten by the Wumpus!")
            self.draw_emoji(next_pos, "💀")
            return
        if next_pos in self.env.pits:
            print("🕳️ The agent fell into a pit!")
            self.draw_emoji(next_pos, "💀")
            return

        self.draw_world()
        self.master.after(1000, self.step)

    def update_gui(self):
        self.draw_world()

if __name__ == "__main__":
    root = tk.Tk()
    app = Game(root)
    root.mainloop()
