#############################################
############ Advent of Code 2022 ############
################# Day 8 #####################
#############################################
import re
import numpy as np


def readData(path):
    return np.genfromtxt(path, delimiter=1, dtype=np.int32)


def firstPart(data):
    row, col = data.shape
    seen_array = np.zeros((row, col))

    for _ in range(
        4
    ):  # idea is to rotate the array 4 times, and go over the array 4 times
        for i, line in enumerate(data):  # each line of the array, plus the line index i
            highest = -1
            for j, num in enumerate(line):
                if num > highest:
                    # if number is higher than highest seen so far, i.e. its visible from the outside
                    highest = num
                    seen_array[i, j] = 1  # keep track of which trees were seen already

        data = np.rot90(data)
        seen_array = np.rot90(seen_array)

    return np.sum(seen_array)


def viewing_distance(n, array):
    view = 1
    if not np.size(array):
        return 0
    for i in array:
        if i < n:
            view += 1
        else:
            return min(view, len(array))
    return min(view, len(array))


def secondPart(data):
    scenic_scores = []
    for i, line in enumerate(data):

        for j, num in enumerate(line):
            right = viewing_distance(num, line[j + 1 :])
            left = viewing_distance(num, np.flip(line[:j]))
            up = viewing_distance(num, np.flip(data[:i, j]))
            down = viewing_distance(num, data[i + 1 :, j])
            scenic_scores.append(right * up * down * left)

    return max(scenic_scores)


if __name__ == "__main__":
    path = "data/day8.txt"
    data = readData(path)
    part1 = firstPart(data)
    part2 = secondPart(data)
    print(f"Solution for part1: {part1}")
    print(f"Solution for part2: {part2}")
