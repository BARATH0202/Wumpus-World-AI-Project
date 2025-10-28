from environment import Environment
from agent import Agent

def run_simulation():
    env = Environment()
    agent = Agent(env)

    print("🏁 Starting Wumpus World Simulation")
    print(f"Wumpus at {env.wumpus_pos}, Gold at {env.gold_pos}, Pits at {env.pits}\n")

    while agent.alive and not agent.has_gold:
        next_move = agent.next_move()
        if next_move is None:
            print("😕 No more safe moves. Exiting...")
            break
        agent.move(*next_move)

    if agent.has_gold:
        print("🎉 Agent won!")
    elif not agent.alive:
        print("💀 Agent lost!")
    else:
        print("🏳️ Agent stopped exploring.")

if __name__ == "__main__":
    run_simulation()
