# graph_coloring_cps
Graph Coloring Algorithm using Backtracking Search AC-3

This repository contains a Python implementation of the graph coloring algorithm using the Backtracking Search technique. The algorithm aims to color the nodes of a graph with a given number of colors, such that no two adjacent nodes share the same color.

The main features of the code include:
- Backtracking Search algorithm implementation for graph coloring
- AC-3 algorithm for enforcing arc consistency
- Visualization of the graph coloring process using NetworkX and Matplotlib

Usage:
1. Create a graph by defining the edges using `add_edge` function in NetworkX.
2. Run the `main` function, which prompts the user to enter the number of colors.
3. The algorithm attempts to color the graph using the specified number of colors.
4. If a valid coloring is found, the nodes with their assigned colors are printed.
5. If no valid coloring is possible, a corresponding message is displayed.
6. The graph coloring process is visualized using a plot.

Contributions and improvements to the code are welcome!
insparations from : 
https://github.com/speix/sudoku-solver/blob/master/sudoku.py
