import time
import random

# Placeholder for HPG-MAPF algorithm import
# from hpg_mapf import HPG_MAPF

def test_scalability(num_agents):
    start_time = time.time()
    # Simulate HPG-MAPF algorithm execution with the given number of agents
    # hpg_mapf = HPG_MAPF(num_agents)
    # hpg_mapf.run()

    # Simulate a delay based on number of agents
    time.sleep(random.uniform(0.1, 0.5) * num_agents / 1000)  # Simulated time complexity
    elapsed_time = time.time() - start_time
    print(f"Performance with {num_agents} agents: {elapsed_time:.2f} seconds")

if __name__ == '__main__':
    agent_counts = [10, 25, 50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000, 10000]
    for count in agent_counts:
        test_scalability(count)