#############################################
########### Advent of Coding 2022 ###########
################# Day 1 #####################
#############################################
from typing import List


def readData(path: str) -> List:
    data = []  # list of lists for calories per elf
    curList = []  # calories carried by current elf
    with open(path, "r") as f:
        for l in f.readlines():
            if l == "\n":  # end of supply for one elf
                data.append(curList)
                curList = []  # reset current inventory
            else:
                curList.append(int(l))  # attach element to current inventory
    data.append(curList)
    return data


#### First part: Elf carrying the maximum number of calories
def findMax(data: List) -> int:
    curMax = 0
    for inv in data:
        if sum(inv) > curMax:
            curMax = sum(inv)

    return curMax


#### Second part: Sum of top 3 elves carrying most calories
def findTop3(data: List) -> int:
    top3Cals = [0]
    minCal = 0
    for inv in data:
        if sum(inv) > minCal:
            if len(top3Cals) > 2:
                top3Cals.remove(minCal)
            top3Cals.append(sum(inv))
            minCal = min(top3Cals)
        assert len(top3Cals) <= 3, "List exceeded length 3"

    assert len(top3Cals) == 3, "Final list does not have 3 elements"
    return sum(top3Cals)


if __name__ == "__main__":
    path = "data/day1.txt"
    data = readData(path)
    part1 = findMax(data)
    part2 = findTop3(data)
    print(f"The solution for part 1 is: {part1}")
    print(f"The solution for part 2 is: {part2}")
