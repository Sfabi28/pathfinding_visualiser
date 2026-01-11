# A* Pathfinding Visualizer

![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/pathfinding_visualizer?style=for-the-badge&color=blue)

A robust, interactive, and real-time visualization tool for the **A* Search Algorithm** built with Python and Pygame. It demonstrates the efficiency of heuristic-based pathfinding, featuring dynamic wall placement, instant feedback, and optimized data structures (`PriorityQueue` & `Hash Set`).

## 📁 1. Installation

Ensure you have **Python 3.x** installed. To keep your environment clean, using a virtual environment (`venv`) is recommended.

**Directory Structure:**
```text
/pathfinding_visualizer
    ├── main.py             <--- RUN THIS FILE
    ├── algorithm.py        (Core A* Logic)
    ├── node.py             (Cell/Node Class)
    └── requirements.txt    (Dependencies)
```

## 2. Setup commands

Clone the repository and install dependencies:

```bash
git clone [https://github.com/Sfabi28/pathfinding_visualizer.git](https://github.com/Sfabi28/pathfinding_visualizer.git)
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