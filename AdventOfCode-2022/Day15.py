#############################################
############ Advent of Code 2022 ############
################# Day 14 ####################
#############################################
import re
from tqdm import tqdm


class Sensor:
    def __init__(self, location, closest_beacon):
        self.location = location
        self.closest_beacon = closest_beacon
        # calculate radius
        self.radius = self.manhattan(self.location, self.closest_beacon)
        print(
            f"Sensor with location: {self.location} and beacon: {self.closest_beacon} initialized. Radius = {self.radius}"
        )

    def overlap_in_line(self, line):
        """Given a line number (y coord)
        calculate the overlap of the sensor's coverage with that line
        in number of units

        Args:
            line (int): coordinate of line (y coord)

        Returns:
            int: number of unit overlaps
        """
        self.covered = set()
        # remaining distance on x axis on provided line
        if self.location[1] == line:
            self.covered.update(
                [
                    (x, line)
                    for x in range(
                        self.location[0] - self.radius,
                        self.location[0] + self.radius + 1,
                    )
                ]
            )
        else:

            remaining_dist = (
                -1
                if line
                not in range(
                    self.location[1] - self.radius, self.location[1] + self.radius + 1
                )
                else self.radius - abs(self.location[1] - line)
            )
            if remaining_dist > -1:
                self.covered.update(
                    [
                        (x, line)
                        for x in range(
                            self.location[0] - remaining_dist,
                            self.location[0] + remaining_dist + 1,
                        )
                    ]
                )

            # breakpoint()

    @staticmethod
    def manhattan(p1, p2):
        """Manhattan distance between two points

        Args:
            p1 (tuple): point 1's coordinates (x, y)
            p2 (tuple): point 2's coordinates
        Return: (int): Manhattan distance between p1 and p2
        """
        dist = 0  # distance between two points
        assert len(p1) == len(p2), "Two points are not in same dimensions!"
        for x1, x2 in zip(p1, p2):  # iterate over both points' coordinates
            # increase distance with absolute (positive) difference between two coords on given axis
            dist += abs(x1 - x2)
        return dist


class System:
    """Represent a system of sensors"""

    def __init__(self, path):
        self.sensors = []
        self.locations = set()
        self.beacons = set()
        with open(path, "r") as f:
            for line in f.readlines():
                # get location of sensor
                location = re.findall(r"Sensor at x=(\W{0,1}\d+), y=(\W{0,1}\d+)", line)
                assert (len(location) == 1) and len(
                    location[0]
                ) == 2, "Sensor coordinates invalid!"
                x, y = list(map(int, location[0]))  # convert to integers
                beacon_location = re.findall(
                    r"beacon is at x=(\W{0,1}\d+), y=(\W{0,1}\d+)", line
                )
                assert (len(beacon_location) == 1) and len(
                    beacon_location[0]
                ) == 2, "Beacon coordinates invalid!"
                bx, by = list(map(int, beacon_location[0]))  # convert to integers
                new_sensor = Sensor((x, y), (bx, by))
                self.locations.add((x, y))
                self.beacons.add((bx, by))
                self.sensors.append(new_sensor)

    def total_overlap(self, line):
        ### Used for part1
        # set of sensor and beacon locations
        locations = set([s.location for s in self.sensors])
        beacon_locations = set([s.closest_beacon for s in self.sensors])
        total_set = set()
        for sen in tqdm(self.sensors):
            sen.overlap_in_line(line)
            total_set.update(sen.covered)

        print(f"Total overlap: {len(total_set - locations.union(beacon_locations))}")
        return total_set

    def uncovered(self, x, y):
        # returns true if x, y is covered by any sensor AND is not a beacon location
        # used in part2
        for sensor in self.sensors:
            if sensor.manhattan((x, y), sensor.location) <= sensor.radius:
                return False
        return True  # if this position is not covered at all

    def search_possible_location(self, limits=4_000_000):
        """
        Used for part 2. Idea is to:
        Iterate over all sensors and for each:
            for each point just outside the border:
                check if point is contained in any sensors's range AND not a beacon:
                    eventually we find a point not in coverage

        """
        for sensor in tqdm(self.sensors):
            for x_movement in range(sensor.radius + 2):  # movement on x-axis
                y_movement = sensor.radius + 1 - x_movement
                # remainder is movement on y-axis
                # offset the movement on both axes into all four directions
                for x_direction, y_direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    # X, Y coordinates for points just outside border
                    # sensor location + move
                    X = sensor.location[0] + (x_movement * x_direction)
                    Y = sensor.location[1] + (y_movement * y_direction)
                    # breakpoint()
                    if (X > limits) or (X < 0) or (Y > limits) or (Y < 0):
                        continue
                    elif self.uncovered(X, Y):
                        return (X * 4_000_000) + Y


if __name__ == "__main__":
    path = "data/day15.txt"
    system = System(path)
    linenum = 2_000_000
    system.total_overlap(linenum)
    part2 = system.search_possible_location()
    print(f"Solution for part 2: {part2}")
