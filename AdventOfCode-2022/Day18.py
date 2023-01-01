#############################################
############ Advent of Code 2022 ############
################# Day 18 ####################
#############################################
from collections import deque
from tqdm import tqdm


class LavaDrop:
    def __init__(self, path):

        self.cubes = []  # store each cube as a triple (x, y, z)
        # for future use, store minimum and maximum of each axis
        self.max = {"x": 0, "y": 0, "z": 0}
        self.min = {"x": 1e10, "y": 1e10, "z": 1e10}
        with open(path, "r") as f:
            for line in f.readlines():
                # create cube coordinate triple from input file
                cube = [int(i) for i in line.strip().split(",")]
                # at each line update the min-max dictionaries if new min/max found
                for key, coord in zip(self.max.keys(), cube):
                    self.max[key] = max(self.max[key], coord)
                    self.min[key] = min(self.min[key], coord)
                self.cubes.append(tuple(cube))
        # also store cubes as set
        self.cubes_set = set(self.cubes)

    ### PART 1
    def connected_cubes(self, cubes: set):
        """
        How many sides of the lava droplet has 'free' sides.
        Approach:
        - iterate over each cube
            - generate all 6 neighbouring cube coordinates
            - check for all generated neighbour coordinates whether they are contained in input data
            - if not contained: increase result counter by one
        """
        freestanding_sides = 0  # track result
        for cube in cubes:  # iterate over each cube
            # calculate all 6 neighbour's coordinates
            coords = self.get_neighbour_coordinates(cube)
            for neighbour_cube in coords:
                # check if a neighbour is empty or is a lava droplet
                if neighbour_cube not in cubes:
                    freestanding_sides += 1  # increase if empty cube
        return freestanding_sides

    def surface_area(self):
        """
        Calculate outer surface area of the lava droplet, following a similar approach to part1:
        Outline of approach:
        - Start from an outer cube position:
            - using BFS explore all cubes that are NOT lava droplets.
            - Store coordinates of all 'air cubes'
        - generate set of all possible coordinates in a large cube
                            (containing the entire droplet PLUS ONE MARGIN)
        - take set difference between all coordinates and air cubes
        - run the previous algorithm on this set
        """
        # list of all possible coordinates in an inclusive cube
        all_coordinates = [
            (x, y, z)
            for x in range(self.min["x"] - 1, self.max["x"] + 2)
            for y in range(self.min["y"] - 1, self.max["y"] + 2)
            for z in range(self.min["z"] - 1, self.max["z"] + 2)
        ]
        air_pockets = set()  # coordinates of air cubes
        queue = deque([])  # queue for BFS
        # determine start point as smallest coordinate in cube
        start_point = tuple(self.min[key] - 1 for key in self.min.keys())
        queue.append(start_point)
        visited = set()  # keep track of visited cubes
        iter_count = 0  # for debug purposes
        while queue:
            iter_count += 1
            element = queue.popleft()  # new element from queue
            print(f"{element} | Iter count {iter_count}")
            # all engihbour coordinates of element
            neighbour_cubes = self.get_neighbour_coordinates(element)
            for cube in neighbour_cubes:
                # check if:
                # - cube not a lava cube
                # - still within range
                #   check if:
                #   - cube not visited yet
                if (cube not in self.cubes_set) and (cube in all_coordinates):
                    air_pockets.add(cube)
                    if cube not in visited:
                        visited.add(cube)
                        queue.append(cube)
        # get the set of coordinates surrounded with the air cubes calculated above
        lava_drop_coordinates = set(all_coordinates).difference(air_pockets)
        # use the function from part 1 to get the surface area
        surface_area = self.connected_cubes(lava_drop_coordinates)
        print(f"Solution for part 2: {surface_area}")
        return surface_area

    @staticmethod
    def get_neighbour_coordinates(cube):
        """Return the 6 neighbouring coordinates of a cube

        Args:
            cube (tuple): the (x, y, z) coordinate of cube

        Returns:
            list: list of triples in (x, y, z) format
        """
        assert len(cube) == 3, "INVALID COORDINATES"
        x, y, z = cube
        coords = [
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),
        ]

        return coords


if __name__ == "__main__":
    path = "data/day18.txt"
    lava = LavaDrop(path)
    part1 = lava.connected_cubes(lava.cubes_set)
    print(f"Solution for part1: {part1}")
    lava.surface_area()
