#############################################
############ Advent of Code 2022 ############
################# Day 3 #####################
#############################################

from typing import List
from string import ascii_lowercase, ascii_uppercase


def readData(path: str) -> List:
    data = []  # store each rucksack as a string in this list
    with open(path, "r") as f:
        for l in f.readlines():  # for each line
            data.append(l.split("\n")[0])  # get rid of end of line signals

    return data


def constructPriority():
    """Construct a dictionary with the priorities of each letter"""
    priority_dct = {}
    counter = 1
    for char in ascii_lowercase + ascii_uppercase:
        priority_dct[char] = counter
        counter += 1

    return priority_dct


#### Part 1
def sharedItemPriority(data):
    score = 0
    priority = constructPriority()
    for sack in data:
        middle = int(len(sack) / 2)
        firstSack = {}  # store each letter seen in first sack
        for c in sack[:middle]:
            firstSack[c] = True

        for char in sack[middle:]:
            if firstSack.get(char):  # if character already seen in first part
                break
        score += priority[char]  # add priority of common element

    return score


def groupItemPriority(data):
    reformat_data = []  # store groups of three string
    score = 0
    priority = constructPriority()

    while len(data) > 0:
        groupData = []
        while len(groupData) != 3:
            groupData.append(data.pop())
        reformat_data.append(groupData)
    for first, second, third in reformat_data:
        common_char = set([*first]).intersection(set([*second]), set([*third])).pop()
        score += priority[common_char]
    return score


if __name__ == "__main__":
    path = "data/day3.txt"
    data = readData(path)
    part1 = sharedItemPriority(data)
    part2 = groupItemPriority(data)
    print(f"Answer to first part: {part1}")
    print(f"Answer to second part: {part2}")
