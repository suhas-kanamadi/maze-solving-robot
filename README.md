# Autonomous Maze Solver using A* (ROS2)

This project implements a grid-based maze solving system using the A* path planning algorithm. The system computes the shortest path from a start point to a goal and simulates robot traversal using ROS2 and RViz.

--------------------------------------------------

OVERVIEW

The maze is represented as a 2D grid:
0 = free space
1 = obstacle

A* computes the optimal path and the robot follows it in RViz.

--------------------------------------------------

FEATURES

- A* path planning
- Grid-based maze
- RViz visualization
- Simulated robot movement
- Planning + execution pipeline

--------------------------------------------------

TECHNOLOGIES

- ROS2 (Humble)
- Python
- RViz

Libraries:
- heapq
- nav_msgs
- geometry_msgs

--------------------------------------------------

PROJECT STRUCTURE

maze_ws/
└── src/
    └── maze_solver/
        ├── maze_solver/
        │   ├── astar.py
        │   ├── maze.py
        │   └── solver_node.py
        ├── package.xml
        ├── setup.py
        └── setup.cfg

--------------------------------------------------

HOW IT WORKS

1. Maze defined in maze.py
2. A* computes shortest path
3. ROS2 publishes:
   - /map
   - /path
   - /robot
4. RViz visualizes everything

--------------------------------------------------

RUNNING THE PROJECT

cd ~/maze_ws
source /opt/ros/humble/setup.bash
colcon build

source install/setup.bash

ros2 run maze_solver solver

# open RViz in new terminal
rviz2

--------------------------------------------------

RVIZ SETUP

- Add Map → /map
- Add Path → /path
- Add Pose → /robot
- Fixed Frame → map

--------------------------------------------------

ALGORITHM

A* uses:
f(n) = g(n) + h(n)

g(n) = cost from start  
h(n) = Manhattan distance to goal  

--------------------------------------------------

LIMITATIONS

- Static maze only
- No dynamic obstacles
- Full map required

--------------------------------------------------

FUTURE WORK

- Real robot integration
- Dynamic obstacle handling
- Gazebo simulation
- SLAM

--------------------------------------------------

AUTHORS

Suhas Kanamadi
Srijan Das
Suhan Kagawade
Stephen Paul
