# A* Pathfinding Visualizer

![Last Commit](https://img.shields.io/github/last-commit/Sfabi28/pathfinding_visualizer?style=for-the-badge&color=blue)

A robust, interactive, and real-time visualization tool for the **Weighted A* Search Algorithm** built with Python and Pygame.
Unlike standard visualizers, this project features **Weighted Terrain** (Mud and Water), forcing the algorithm to calculate trade-offs between a shorter path and a "cheaper" path (avoiding high-cost terrain).

## 📁 1. Installation

Ensure you have **Python 3.x** installed. To keep your environment clean, using a virtual environment (`venv`) is recommended.

**Directory Structure:**
```text
/pathfinding_visualizer
    ├── main.py             <--- RUN THIS FILE
    ├── algorithm.py        (Core A* Logic)
    ├── node.py             (Cell/Node Class)
    ├── buttons.py          (UI & Button Class)
    └── requirements.txt    (Dependencies)
```

## 2. Setup commands

Clone the repository and install dependencies:

```bash
git clone https://github.com/Sfabi28/pathfinding_visualizer.git
cd pathfinding_visualizer
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
pip install pygame
```

## 🚀 2. First Run

To launch the visualization window, simply run the main script:

```bash
python main.py
```

## ⚙️ 3. Controls & Usage

The tool is fully interactive via Mouse and Keyboard.

```text
Input,Action
Left Click (1st), Place START node (Orange).
Left Click (2nd), Place END node (Turquoise).
Left Click (Hold), Draw WALLS/BARRIERS (Black).
Right Click, Erase nodes or walls.
SPACE Bar, Start the A* Algorithm.
D Key, Reset/Clear the grid.
```

## 📝 4. How it Works

```text
The simulation runs a weighted A* algorithm using Manhattan Distance as the heuristic:

    F Score = G + H

        G (G Score): The exact distance from the Start node to the current node.
        H (Heuristic): The estimated distance from the current node to the End node (ignoring walls).

    Logic Flow:
        1. The algorithm prioritizes nodes with the lowest 'F' score using a PriorityQueue.
        2. It explores neighbors (Up, Down, Left, Right).
        3. If a neighbor offers a shorter path (lower G), the parent link is updated.
        4. This continues until the End node is reached or no path is possible.
```

## 🌍 5. Terrain & Weights

This visualizer uses a Weighted Graph. The algorithm treats different colors as different "costs" to traverse.

```text
Terrain	Color	Weight (Cost)	Effect
Street	⬜ White	1	Default movement speed.
Mud	🟫 Brown	5	Slows down the path. The algorithm will try to go around it.
Water	🟦 Blue	15	Very slow. The algorithm will avoid it unless necessary.
Wall	⬛ Black	∞	Impassable.
```

## 📊 6. Visual Legend

To visualize both the Terrain (what the ground is) and the Algorithm State (what the computer is thinking), the tool uses a layered drawing approach:

    Background Square: Represents the Terrain (White, Brown, or Blue).

    Overlay Circle: Represents the Algorithm's current state.

```text
Algorithm State Colors:

    [GREEN Circle] : Open Set. Nodes discovered/queued for inspection.
    [RED Circle]   : Closed Set. Nodes already visited.
    [PURPLE Circle]: The Path. The optimal route found.
```

## ⌨️ Key behavior (internal actions)

This section explains what happens in the code when pressing keys handled by Pygame (`M`, `R`, `D`). The actions are implemented in [main.py](main.py#L1) and call functions in other modules.

- **`M` (Build / generate maze)**
    - Action: pressing `M` sets `start` and `end` to `None` and calls `generate_maze(...)` in [builder.py](builder.py#L1).
    - What `generate_maze` does: fills the grid with barriers, carves random corridors, resets some cells to open, and finally places the `start` node (top-left) and the `end` node (near the opposite corner). The function returns the `start, end` references used by the main loop.

- **`R` (Partial reset)**
    - Action: pressing `R` calls `reset(grid, ROWS, start, end)` defined in [main.py](main.py#L1).
    - Effect: clears the algorithm state (open/closed/path) from explored cells but does *not* remove walls/barriers nor the `start`/`end` nodes. Nodes with special weights (e.g. `mud`, `water`) keep their `weight` and base color.

- **`D` (Clear / Clear grid)**
    - Action: pressing `D` recreates the grid by calling `make_grid(ROWS, width)`, sets `start = None` and `end = None`, and resets the current brush to `barrier`.
    - Effect: removes all non-UI nodes (full visible map reset), including special terrain cells and user-drawn walls.

Note: the same behaviors are available via the UI buttons (for example the `Build` button calls the same `generate_maze`). For implementation details see [builder.py](builder.py#L1) and [main.py](main.py#L1).