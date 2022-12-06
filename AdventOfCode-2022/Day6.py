#############################################
############ Advent of Code 2022 ############
################# Day 6 #####################
#############################################
from collections import deque


def readData(path):

    with open(path, "r") as f:
        code = f.readline()
    return code


### My legacy solution
def find4NonRepeat(data: str) -> int:
    seen_stack = []
    add = 0  # index where we add the nex character
    delete = 0  # index at the end of window
    while add - delete < 4:
        if data[add] not in seen_stack:
            seen_stack.append(data[add])
            add += 1
        else:
            seen_stack = []
            delete = add
    return add


### Part 2
def findNonRepeat(data: str, n: int) -> int:
    ### This is a more universal solution

    for i in range(len(data)):  # index
        if (
            len(set(data[i : i + n])) == n
        ):  # set makes sure no repeated chars remain in substring
            return i + n


if __name__ == "__main__":
    path = "data/day6.txt"
    data = readData(path)
    part1 = find4NonRepeat(data)
    part2 = findNonRepeat(data, 14)
    print(f"Index for part 1: {part1}")
    print(f"Index for part 2: {part2}")
