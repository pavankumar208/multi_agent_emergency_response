
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

# ----- Environment Setup -----
class EmergencyMap:
    def __init__(self, size):
        self.size = size
        self.graph = nx.grid_2d_graph(size, size)
        self.emergencies = {}  # {(x,y): priority}

    def generate_emergencies(self, count=5):
        for _ in range(count):
            node = (random.randint(0, self.size-1), random.randint(0, self.size-1))
            priority = random.randint(1, 10)
            self.emergencies[node] = priority

    def show_map(self, agents=[]):
        pos = dict((n, n) for n in self.graph.nodes())
        plt.figure(figsize=(8,8))
        
        # Draw grid nodes
        nx.draw(self.graph, pos=pos, node_color='lightblue', with_labels=True, node_size=500)

        # Draw emergencies
        nx.draw_networkx_nodes(self.graph, pos, nodelist=self.emergencies.keys(), node_color='red', node_size=700)

        # Draw agent positions
        for agent in agents:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=[agent.position], node_color='green', node_size=700)
            plt.text(agent.position[0], agent.position[1]+0.2, f"A{agent.id}", fontsize=12, ha='center', color='green')

        plt.title("Emergency Map: Red=Emergencies, Green=Agents")
        plt.show()

# ----- Agent Setup -----
class Agent:
    def __init__(self, agent_id, env: EmergencyMap):
        self.id = agent_id
        self.env = env
        self.position = (0, 0)  # start position (can be randomized)
        self.path = []

    def move_to(self, destination):
        try:
            # Find shortest path on grid graph
            self.path = nx.shortest_path(self.env.graph, source=self.position, target=destination)
            self.position = destination
            print(f"Agent {self.id} moved to {destination} via path: {self.path}")
        except nx.NetworkXNoPath:
            print(f"Agent {self.id} could not find a path to {destination}.")

# ----- Swarm-inspired Target Assignment -----
def assign_targets_swarm(emergencies, agents):
    # Sort emergencies by descending priority
    sorted_emergencies = sorted(emergencies.items(), key=lambda x: -x[1])
    assignments = {}
    for i, agent in enumerate(agents):
        if i < len(sorted_emergencies):
            target = sorted_emergencies[i][0]
            assignments[agent.id] = target
    return assignments

# ----- Main -----
if __name__ == "__main__":
    # Initialize environment
    env = EmergencyMap(size=7)
    env.generate_emergencies(count=7)

    # Create agents
    agents = [Agent(agent_id=i, env=env) for i in range(3)]

    print("Initial map with emergencies and agents:")
    env.show_map(agents)

    # Assign targets to agents based on priority
    assignments = assign_targets_swarm(env.emergencies, agents)

    # Agents move to their assigned emergencies
    for agent in agents:
        target = assignments.get(agent.id)
        if target:
            agent.move_to(target)

    print("\nFinal agent positions on map:")
    env.show_map(agents)
