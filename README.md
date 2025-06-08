
# 🆘 Emergency Response Simulation using Swarm-Inspired Agents

This Python project simulates an emergency response system in a grid-based environment using multiple intelligent agents inspired by swarm behavior. The goal is to assign the highest-priority emergencies to available agents and visualize their movement on the grid.

## 📌 Features

- Grid-based map using **NetworkX**
- Random emergency generation with priority levels (1–10)
- Multiple agents capable of navigating the grid
- **Swarm-inspired** emergency assignment based on priority
- Visualization using **Matplotlib**

## 🛠️ Technologies Used

- **Python 3.x**
- **NetworkX** for grid graph and pathfinding
- **Matplotlib** for visualization
- **NumPy & random** for data generation and control

## 🚦How It Works

1. **Environment Setup**
   - A 2D grid (`size x size`) is created using `networkx.grid_2d_graph`.
   - Emergencies are randomly placed on the grid with a priority score (1-10).

2. **Agent Initialization**
   - Multiple agents (default 3) are placed on the map at position `(0, 0)`.
   - Each agent is capable of moving to a destination via the shortest path.

3. **Swarm-Inspired Target Assignment**
   - Emergencies are sorted by priority.
   - The highest-priority emergencies are assigned to the agents sequentially.

4. **Agent Movement**
   - Each agent moves to its assigned target using the shortest path in the grid.
   - Movement and paths are logged.

5. **Visualization**
   - Initial and final positions of agents and emergencies are displayed on a color-coded map:
     - 🟥 **Red** = Emergencies
     - 🟩 **Green** = Agents
     - 🔵 **Light Blue** = Grid nodes

## 🧪 Example Output

- Initial map with randomly placed emergencies
- Console output showing agent movements and assigned paths
- Final map showing updated agent positions

## 🧾 How to Run

### ✅ Requirements

Install the dependencies:

```bash
pip install networkx matplotlib numpy
```

### ▶️ Run the Script

```bash
python emergency_swarm_simulation.py
```

> Replace `emergency_swarm_simulation.py` with the name of your script file.

## 📷 Sample Visualization

![Emergency Response Map Sample](#)  

## 🔁 Future Improvements

- Add **obstacles** or blocked paths in the environment.
- Introduce **dynamic emergencies** that appear over time.
- Implement **multi-agent cooperation** or communication protocols.
- Assign agents based on **distance and priority**, not just priority.

## 🧑‍💻 Author

**Pavan Kumar**  
AI & ML Researcher | System Simulation Enthusiast  

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
