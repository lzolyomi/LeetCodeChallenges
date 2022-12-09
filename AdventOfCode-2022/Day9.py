#############################################
############ Advent of Code 2022 ############
################# Day 9 #####################
#############################################
from math import copysign


def readData(path):
    moves = []
    with open(path, "r") as f:
        for l in f.readlines():
            moves.append(l.split())

    return moves


def firstPart(data):
    moves_dict = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    H = [0, 0]
    T = [0, 0]
    T_visits = set()

    for direction, repeat in data:
        move_pair = moves_dict[direction]
        for _ in range(int(repeat)):
            for i, tup in enumerate(zip(H, move_pair)):
                pos, move = tup
                H[i] = pos + move
            T = trail_T(T, H)
            T_visits.add(T)
    return len(T_visits)


def trail_T(T, H):
    if abs(H[0] - T[0]) == 2 and abs(H[1] - T[1]) == 2:
        # Trying this new approach for part 2, using the sign
        return H[0] - copysign(1, H[0] - T[0]), H[1] - copysign(1, H[1] - T[1])

    if abs(H[0] - T[0]) == 2:  # vertical move
        # we need to move the tail
        return H[0] - copysign(1, H[0] - T[0]), H[1]
        # Move tail to one position before/after head on x axis
    elif abs(H[1] - T[1]) == 2:  # horizontal move
        # Move tail to one position before/after head on y axis
        return H[0], H[1] - copysign(1, H[1] - T[1])
    return tuple(T)


def secondPart(data):

    moves_dict = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    knots = [
        [0, 0] for _ in range(10)
    ]  # each double represent a knot [0] the head, [9] the tail
    T_visits = set()

    for direction, repeat in data:
        move_pair = moves_dict[direction]
        for _ in range(int(repeat)):
            for i, tup in enumerate(zip(knots[0], move_pair)):
                # move head
                pos, move = tup
                knots[0][i] = pos + move
            for i in range(1, 10):
                knots[i] = trail_T(knots[i], knots[i - 1])
            T_visits.add(knots[-1])
    return len(T_visits)


if __name__ == "__main__":
    path = "data/day9.txt"
    data = readData(path)
    part1 = firstPart(data)
    part2 = secondPart(data)
    print(f"Solution for part1: {part1}")
    print(f"Solution for part2: {part2}")
