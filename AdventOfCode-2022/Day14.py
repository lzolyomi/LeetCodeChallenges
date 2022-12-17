#############################################
############ Advent of Code 2022 ############
################# Day 14 ####################
#############################################


def parse_data(path):
    rocks = []  # store each rock as a list of tuples (pairs)

    with open(path, "r") as f:

        for line in f.readlines():
            allpaths = line.strip().split(" -> ")
            pairs = [
                tuple([int(el.split(",")[0]), int(el.split(",")[1])]) for el in allpaths
            ]
            # [(514, 127), (518, 127)]
            #   x     y      x    y
            # x: distance from left edge
            # y: distance from top
            rocks.append(pairs)

    return rocks


class Rockscan:
    def __init__(self, data, floor=False):
        self.data = data  # store original data
        self.blocks = set()  # store position of blocking elements (rocks and sand)

        for line in data:  # each rock structure
            for i in range(1, len(line)):  # each pair of positions
                p1, p2 = line[i - 1], line[i]
                # range on x axis on which the two points p1, p2 span
                xrange = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
                # range on y axis on which the two points p1, p2 span
                yrange = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)
                points = [(x, y) for x in xrange for y in yrange]
                self.blocks.update(points)

        self.depth = max([x[1] for x in self.blocks])
        ###### Modifications for second part
        self.floor_depth = None  # not used in first part
        self.floor = floor
        if self.floor:  # construct floor for part 2
            self.floor_depth = self.depth + 2
        print(
            f"Rock structure build with {len(self.blocks)} rock units and depth of {self.depth}"
        )
        self.num_rocks = len(self.blocks)

    def pour_sand(self):
        sand_count = 0
        overflow = False  # sets true if sand overflows
        while not overflow:
            sand_position = self.release_unit_sand()
            if not sand_position:
                overflow = True
            else:
                assert type(sand_position) == tuple, "Sand position is not tuple"
                sand_count += 1
        if not self.floor:
            print(f"Total amount of sand poured into structure: {sand_count}")

    def release_unit_sand(self):
        pour_position = (500, 0)  # x, y coordinate of entry position for sand
        cur_pos = pour_position
        moves = True
        while moves:
            if self.move_sand(cur_pos) == "OVERFLOW":
                print("Sand overflows")
                moves = False  # sand overflows
                return False
            elif self.move_sand(cur_pos) == "ENTRY-BLOCK":
                moves = False
                return False

            elif c := self.move_sand(cur_pos):  # returns a new position
                cur_pos = c
                # print(f"Sand moved to position {cur_pos}")

            elif self.move_sand(cur_pos) == False:
                # print("Sand came to rest")
                moves = False
                self.blocks.add(cur_pos)
                return cur_pos  # if sand came to rest, return its position

    def move_sand(self, current_position):
        x, y = current_position
        if (y >= self.depth) & (not self.floor):  # sand falls down
            return "OVERFLOW"
        elif y + 1 == self.floor_depth:
            return False
        elif (x, y + 1) not in self.blocks:  # sand can fall down
            return (x, y + 1)

        elif (
            x - 1,
            y + 1,
        ) not in self.blocks:  # sand falls down and to the left
            return (x - 1, y + 1)

        elif (x + 1, y + 1) not in self.blocks:  # sand falls down and to the right
            return (x + 1, y + 1)

        else:  # sand cannot move any further from this position
            if (x, y) == (500, 0):
                print(
                    f"Sand covering entry hole with {len(self.blocks) + 1 - self.num_rocks} blocks of sand"
                )
                return "ENTRY-BLOCK"
            return False


if __name__ == "__main__":
    path = "data/day14.txt"
    data = parse_data(path)
    rock = Rockscan(data)
    rock.pour_sand()
    # part 2
    rock = Rockscan(data, floor=True)
    rock.pour_sand()
