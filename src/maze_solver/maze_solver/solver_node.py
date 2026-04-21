import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path, OccupancyGrid
from geometry_msgs.msg import PoseStamped

from .maze import maze, start, goal
from .astar import astar

import math


class MazeSolver(Node):
    def __init__(self):
        super().__init__('maze_solver')

        self.path_pub = self.create_publisher(Path, '/path', 10)
        self.map_pub = self.create_publisher(OccupancyGrid, '/map', 10)
        self.robot_pub = self.create_publisher(PoseStamped, '/robot', 10)

        # ✅ CLEAN PATH (A* already fixed)
        self.path = astar(maze, start, goal)

        self.index = 0
        self.timer = self.create_timer(0.5, self.animate)

    def animate(self):
        self.publish_map()

        if self.path and self.index < len(self.path):
            current = self.path[self.index]

            next_pos = None
            if self.index + 1 < len(self.path):
                next_pos = self.path[self.index + 1]

            self.publish_robot(current, next_pos)
            self.publish_partial_path(self.path)

            self.index += 1

    def publish_map(self):
        grid = OccupancyGrid()
        grid.header.frame_id = "map"

        rows = len(maze)
        cols = len(maze[0])

        grid.info.resolution = 1.0
        grid.info.width = cols
        grid.info.height = rows

        data = []
        for row in maze:
            for cell in row:
                data.append(100 if cell == 1 else 0)

        grid.data = data
        self.map_pub.publish(grid)

    def publish_robot(self, pos, next_pos=None):
        msg = PoseStamped()
        msg.header.frame_id = "map"

        x, y = pos

        msg.pose.position.x = float(y)
        msg.pose.position.y = float(x)
        msg.pose.position.z = 0.0

        if next_pos:
            nx, ny = next_pos

            dx = ny - y
            dy = nx - x
            yaw = math.atan2(dy, dx)

            msg.pose.orientation.z = math.sin(yaw / 2.0)
            msg.pose.orientation.w = math.cos(yaw / 2.0)

        self.robot_pub.publish(msg)

    def publish_partial_path(self, partial):
        path_msg = Path()
        path_msg.header.frame_id = "map"

        for (x, y) in partial:
            pose = PoseStamped()
            pose.header.frame_id = "map"
            pose.pose.position.x = float(y)
            pose.pose.position.y = float(x)
            pose.pose.position.z = 0.0
            path_msg.poses.append(pose)

        self.path_pub.publish(path_msg)


def main(args=None):
    rclpy.init(args=args)
    node = MazeSolver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
