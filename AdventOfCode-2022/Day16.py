#############################################
############ Advent of Code 2022 ############
################# Day 16 ####################
#############################################

import re
from tqdm import tqdm
from collections import deque


class Valve:
    """
    Represents a valve with its id (two char name),
    flow rate as integer and
    lists of valves we can go to from there
    """

    def __init__(self, id, flow_rate, tunnels):
        self.id = id
        self.flow = int(flow_rate)
        self.tunnels = tunnels
        # initialize a dictionary storing distance to each valve
        # distance to self is always zero, NOTE: may add: , "AA": 0
        self.distances = {"AA": 0}

    def add_distance(self, id, dist):
        assert id not in self.distances, "This valve has already been added!"
        if self.id not in self.distances:
            self.distances[self.id] = 0  # add own distance as 0 if not added
        self.distances[id] = dist

    def __repr__(self):
        return f"Valve {self.id}"


class ValveSystem:
    """
    Represent the entire input data with valves.
    This class does the followings:
    - Parse input data, initialize each valve and store in it self.valves
    - Truncate graph to only non-zero flow valves
        - calculate distances between any two non-zero vertices
        - store the distances for each valve
    """

    def __init__(self, path):
        self.valves = {}  # dictionary of valves

        with open(path, "r") as f:
            for line in f.readlines():
                valve = re.findall(r"Valve (\w{2})", line)[0]
                flow_rate = re.findall(r"rate=(\d+)", line)[0]
                connects_to = re.findall(r"([A-Z]{2}|[A-Z]{2}\,)+", line.split("to")[1])
                self.valves[valve] = Valve(valve, flow_rate, connects_to)
                # initialize Valve object and store with its id as key
        print(f"Data parsed, {len(self.valves)} valves found!")
        print(f"Calculating distances...")

        ### Perform BFS and calculate distances to all non-zero flow nodes
        for valve in self.valves.values():
            # iterate over each valve
            if (valve.flow == 0) & (valve.id != "AA"):
                # ignore valves with zero flow that are not start points
                continue
            # Initialize FIFO queue for the selected valve.
            # It will be used for the BFS algorithm
            queue = deque([(valve, 0)])
            visited = {valve.id}  # set of nodes already visited from this node
            while queue:  # as long as queue is not empty
                # remove first element from queue
                valve_object, distance = queue.popleft()
                # iterate over each neighbour for the given valve
                for neighbour_id in valve_object.tunnels:
                    if neighbour_id in visited:  # only visit each node once
                        continue

                    visited.add(neighbour_id)  # add neighbour valve to visited
                    neighbour = self.valves[
                        neighbour_id
                    ]  # retrieve valve object from ID
                    queue.append(
                        (neighbour, distance + 1)
                    )  # append neighbour to end of queue
                    #                           ^ increase distance by one when appending to queue
                    if neighbour.flow > 0:
                        # if neighbour has nonzero flow, add its distance to the valve's distances dict
                        valve.add_distance(neighbour.id, distance + 1)
            del valve.distances[valve.id]
            if valve.id != "AA":
                del valve.distances["AA"]
        ### Preparations for DFS

        self.memo = {}  # dictionary for memoization
        self.valve_index_positions = {  # index positions for valves
            v.id: idx
            for idx, v in enumerate(
                [val for val in self.valves.values() if val.flow > 0]
            )
        }

    def dfs(self, minutes: int, valve_pos: Valve, valve_mask):
        # state is identified with three properties:
        # - elapsed minutes
        # - current position (which valve)
        # - which valves are open (using a bitmask)
        # start with checking the memo if current state seen:

        if (minutes, valve_pos.id, valve_mask) in self.memo:
            return self.memo[(minutes, valve_pos.id, valve_mask)]

        maximum = 0  # maximum flow throughtput at the moment
        for neighbour in valve_pos.distances.keys():
            # use a bitwise map to keep track of which valves are open
            # bitmap:          0 0 1 0 1 0 := binary map: 2 + 8 = 10
            # valve ids        J H E D C B
            # valve positions: 5 4 3 2 1 0   (stored in valve_index_positions)
            # this bitmap means that valves E and C are open
            #################################################
            # create the bit signing the current valve. e.g.;
            # valve DD: 0 0 0 1 0 0
            bit = 1 << self.valve_index_positions[neighbour]
            # obtain neighbour Valve object
            neighbour_object = self.valves[neighbour]
            if valve_mask & bit:
                # if valve is already open, as signed in the valve_mask
                continue
            # remaining time is: current minutes remaining - distance to neighbour valve - 1
            #                           ^                       ^                          ^
            #            passed as function arg       stored in Valve obj      time to open valve
            remtime = minutes - valve_pos.distances[neighbour] - 1
            if remtime <= 0:
                # if there is no time to go there & open the valve, skip it
                continue
            # set maximum as either current maximum, or the new maximum if we go down on that route
            maximum = max(
                maximum,  # current value of maximum
                self.dfs(
                    remtime, neighbour_object, valve_mask | bit
                )  # flowrate explored in this state
                + remtime * neighbour_object.flow,
                # flow gained := remaining time * flow per minute of current (neighbour valve)
            )
        self.memo[(minutes, valve_pos.id, valve_mask)] = maximum
        return maximum

    def two_agents(self):
        """Simulate the two agent version of the previous game
        The idea here is the following:
        - use the same DFS function as above, but with a few tweaks:
            - we run it twice per iteration, on two exclusive subset of all valves
            - manipulate the bitmask such that they signal the 'excluded' valves are open
                                                                    (but we do not add flow for them)
            - check all possible combination of subsets, sum up the max flow from both
            - store the maximum and return it as answer
        """
        maximum = 0  # maximum value seen so far
        bitmax = (1 << len(self.valve_index_positions)) - 1
        # size of the total bitmap used to denote valves open/close
        # working of the split is the following
        # lets say we have 6 valves
        # bitmax =       1 1 1 1 1 1
        # positions      6 5 4 3 2 1
        # split these two up into two exclusive sets, i.e.;
        # split 1 :=     0 0 0 1 1 0
        # split 2 :=     1 1 1 0 0 1
        #                ___________|-
        # bitmax =       1 1 1 1 1 1
        for split in tqdm(range(bitmax + 1)):
            maximum = max(
                maximum,
                self.dfs(26, self.valves["AA"], split)
                + self.dfs(26, self.valves["AA"], split ^ bitmax),
            )

        return maximum


if __name__ == "__main__":
    path = "data/day16.txt"
    sys = ValveSystem(path)
    part1 = sys.dfs(30, sys.valves["AA"], 0)
    print(f"Result for part 1: {part1}")
    part2 = sys.two_agents()
    print(f"Result for part 2: {part2}")
