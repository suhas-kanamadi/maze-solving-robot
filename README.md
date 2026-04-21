# Autonomous Maze Solver using A* (ROS2)

This project implements a grid-based maze solving system using the A* path planning algorithm. The system computes the shortest path from a start point to a goal and simulates robot traversal using ROS2 and RViz.

---

## Overview

The maze is represented as a 2D grid where:
- 0 represents free space
- 1 represents obstacles

The A* algorithm is used to compute the optimal path. The result is visualized in RViz along with a simulated robot that follows the computed path step-by-step.

---

## Features

- A* path planning algorithm
- Grid-based maze representation
- Real-time visualization using RViz
- Simulated robot movement along planned path
- Clear separation between planning and execution

---

## Technologies Used

- ROS2 (Humble)
- Python
- RViz (for visualization)

Libraries:
- heapq (priority queue)
- nav_msgs (Path, OccupancyGrid)
- geometry_msgs (PoseStamped)

---

## Project Structure
