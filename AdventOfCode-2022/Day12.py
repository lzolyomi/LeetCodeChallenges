#############################################
############ Advent of Code 2022 ############
################# Day 12 ####################
#############################################
from string import ascii_lowercase
import numpy as np
from collections import deque


def height_dict():
    dct = {}
    for num, char in enumerate(ascii_lowercase):
        dct[char] = num
    dct["E"] = dct["z"]
    dct["S"] = dct["a"]
    return dct


class Node:
    def __init__(self, pos, height, start=False):
        height_conversion = height_dict()
        self.pos = pos  # position in (x, y), also serves as ID for a node
        self.height = height if isinstance(height, int) else height_conversion[height]
        self.connections = []
        # store start and end nodes in specific
        self.start = start  # starting node for BFS
        self.end = False  # end node for BFS
        self.__dist = (
            0 if self.start else -1
        )  # distance from start node. -1 used for debugging

    def __repr__(self):
        return f"Node at position {self.pos} with height: {self.height} | start node: {self.start} | distance from start: {self.__dist} | num. connections: {len(self.connections)}"

    def add_connection(self, node):
        if isinstance(node, Node):
            self.connections.append(node)
        else:  # iterable
            self.connections += node

    def set_distance(self, n):
        self.__dist = n

    def get_distance(self):
        assert self.__dist >= 0, "Node with negative distance tried to be accessed!"
        return self.__dist


def evaluate_directions(i, j, array, direction):
    assert direction in ["left", "right", "up", "down"], "Invalid direction!"
    row, col = array.shape
    if direction == "right":
        if j == col - 1:  # on the right edge
            return None, None
        else:
            return array[i, j + 1], (i, j + 1)
    if direction == "left":
        if j == 0:  # on the left edge
            return None, None
        else:
            return array[i, j - 1], (i, j - 1)
    if direction == "up":
        if i == 0:  # on the top
            return None, None
        else:
            return array[i - 1, j], (i - 1, j)
    if direction == "down":
        if i == row - 1:  # on the right edge
            return None, None
        else:
            return array[i + 1, j], (i + 1, j)


def parseInput(path):
    data = []
    with open(path, "r") as f:
        for line in f.readlines():
            data.append([key for key in list(line.strip())])
    array = np.array(data)
    return array


class BFS:
    def __init__(self, array):
        for i, line in enumerate(array):
            for j, item in enumerate(line):
                if item == "S":
                    start_node = Node((i, j), 0, start=True)
                if item == "E":
                    end_position = (i, j)

        self.start_node = start_node
        self.end_position = end_position
        self.array = array

    def __repr__(self):
        return f"BFS with start position: {self.start_node.pos}, end position: {self.end_position} | array size: {self.array.shape}"

    def do_bfs(self):
        visited = {self.start_node.pos: 0}  # store all visited nodes' coordinates
        queue = deque([self.start_node])  # queue for BFS
        height_conversion = height_dict()
        while queue:  # until queue is not empty
            # print(f"Size of queue: {len(queue)} |", end=" ")
            current = queue.popleft()  # get first node out of queue (FIFO structure!)
            row, col = current.pos  # 2D position of current node
            # print(
            #     f"Height: {current.height} ||| Position: {current.pos} | total visited: {len(visited)} | distance from start: {current.get_distance()} "
            # )
            for d in ["left", "right", "up", "down"]:  # explore in all directions
                letter, pos = evaluate_directions(row, col, self.array, d)
                # evaluate given direction, returning letter and position
                if (letter and pos) and (pos not in visited):  # if direction inside box
                    # if height difference between current node and newly discovered one is at most 1
                    if (height_conversion[letter] - current.height) <= 1:
                        if pos == self.end_position:
                            print(
                                f"END IS REACHED! with a distance of {current.get_distance() + 1}"
                            )
                            return current.get_distance() + 1
                        # create new node
                        new_node = Node(pos, height_conversion[letter])
                        # set distance of new node to one higher than what current node has
                        new_node.set_distance(current.get_distance() + 1)
                        new_node.add_connection(current)
                        # connect new node to current node
                        current.add_connection(new_node)
                        queue.append(new_node)

                        visited[pos] = current.get_distance() + 1

        # for key, value in visited.items():
        #     self.array[key[0], key[1]] = str(value)

        # for line in self.array:

        #     print("|".join(list(line)))
        return float(np.inf)


def findPart2(array, initial_start):
    shortestPaths = []
    array[initial_start[0], initial_start[1]] = "a"
    for i, line in enumerate(array):
        for j, item in enumerate(line):
            if item == "a":
                copy = np.copy(array)
                copy[i, j] = "S"
                bfs = BFS(copy)
                shortestPaths.append(bfs.do_bfs())

    print(f"LOWEST distance from 'a': {min(shortestPaths)}")


if __name__ == "__main__":
    path = "data/day12.txt"
    array = parseInput(path)
    bfs = BFS(array)
    bfs.do_bfs()
    findPart2(array, bfs.start_node.pos)
