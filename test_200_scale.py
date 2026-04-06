# Large-Scale Simulation with 200 Agents

import random
import time
import numpy as np

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, grid_size):
        self.x = (self.x + random.choice([-1, 0, 1])) % grid_size
        self.y = (self.y + random.choice([-1, 0, 1])) % grid_size


def run_simulation(num_agents, grid_size, timesteps):
    agents = [Agent(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(num_agents)]
    positions = np.zeros((num_agents, 2, timesteps))  # x and y positions

    for t in range(timesteps):
        for i, agent in enumerate(agents):
            agent.move(grid_size)
            positions[i, 0, t] = agent.x
            positions[i, 1, t] = agent.y

    return positions


def benchmark_simulation(num_agents, grid_size, timesteps):
    start_time = time.time()
    run_simulation(num_agents, grid_size, timesteps)
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    num_agents = 200
    grid_size = 100
    timesteps = 500
    duration = benchmark_simulation(num_agents, grid_size, timesteps)
    print(f'Simulation completed in {duration:.2f} seconds.')  
