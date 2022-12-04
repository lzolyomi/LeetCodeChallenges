#############################################
############ Advent of Code 2022 ############
################# Day 4 #####################
#############################################
from typing import List


def readData(path: str) -> List:
    data = []  #
    currentPair = []
    with open(path, "r") as f:
        for l in f.readlines():
            assignment = l.split(",")  # split two range assignment
            assert len(assignment) == 2
            for a in assignment:
                s = a.split("-")
                currentPair.append((int(s[0]), int(s[1])))
            data.append(currentPair)
            currentPair = []

    return data


def checkTotalOverlap(data):
    overlapCounter = 0
    for first, second in data:  # one pair of elves with their range (first, second)
        firstRange = list(range(first[0], first[1] + 1))
        secondRange = list(range(second[0], second[1] + 1))
        if set(firstRange).issubset(secondRange):
            overlapCounter += 1
        elif set(secondRange).issubset(firstRange):
            overlapCounter += 1

    return overlapCounter


def checkOverlapExists(data):
    overlapCounter = 0
    for first, second in data:  # one pair of elves with their range (first, second)
        firstRange = list(range(first[0], first[1] + 1))
        secondRange = list(range(second[0], second[1] + 1))
        if len(set(firstRange).intersection(secondRange)) > 0:
            print(f"Ranges {first} and {second} overlap!")
            overlapCounter += 1

    return overlapCounter


if __name__ == "__main__":
    path = "data/day4.txt"
    data = readData(path)
    part1 = checkTotalOverlap(data)
    part2 = checkOverlapExists(data)
    print(f"Result from first part: {part1}")
    print(f"Result from second part: {part2}")
