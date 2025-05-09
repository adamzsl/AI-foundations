# AI-foundations

This project contains implementations of several TSP algorithms and utilities:

- lab1/route_search.py – BFS & DFS for TSP
- lab2/greedy.py – Nearest Neighbour & basic greedy TSP
- lab3/astar.py – A\* search for TSP

## Running

Always run modules via `-m` from the project root:

```bash
python -m lab3.astar
```

Why `-m`?

- Runs `lab3.astar` _as a module_ in its package context
- Ensures the project root is on `sys.path` so `from lab1.route_search import …` works
- Sets `__name__ == "__main__"` inside the script
