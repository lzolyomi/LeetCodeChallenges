#############################################
############ Advent of Code 2022 ############
################# Day 5 #####################
#############################################

from collections import deque
import re


def readData(path: str) -> tuple:
    instructions = []
    ### Check for number of columns
    prev = None  ## store previous line
    with open(path, "r") as f:
        for l in f.readlines():
            if l == "\n":
                break
            prev = l
    num_cols = max([int(i.strip()) for i in prev.split("  ")])

    ### Retrieve crate structure in columns
    crate_structure = [deque() for _ in range(num_cols)]
    crate_match = re.compile(r"(   |\[.\]) ?" * 9)
    with open(path, "r") as f:
        for l in f.readlines():
            if len(crate_match.findall(l)) == 0:
                break
            for i, item in enumerate(crate_match.findall(l)[0]):
                if len(item.strip()) > 0:
                    crate_structure[i].appendleft(item)

    ### Retrieve move instructions
    instr_match = re.compile("move (\d+) from ([1-9]) to ([1-9])")
    with open(path, "r") as f:
        for l in f.readlines():
            matches = instr_match.findall(l)
            if len(matches) > 0:  # if instruction found
                matches = matches[0]
                dct = {
                    "amount": int(matches[0]),
                    "from": int(matches[1]),
                    "to": int(matches[2]),
                }
                instructions.append(dct)
    return crate_structure, instructions


### First part
def moveCrates(crates, instructions):

    for line in instructions:
        for _ in range(line.get("amount")):
            elem = crates[line.get("from") - 1].pop()
            crates[line.get("to") - 1].append(elem)
    print("Boxes on top of each stack: ")
    for dq in crates:
        print(dq[-1], end=" ")

    return crates


def crateMover9001(crates, instructions):

    for line in instructions:
        elements = deque()
        for _ in range(line.get("amount")):
            if len(crates[line.get("from") - 1]) > 0:  # if stack not empty
                elem = crates[line.get("from") - 1].pop()
                elements.appendleft(elem)
        crates[line.get("to") - 1] += elements
    print("\n Boxes on top of each stack for CrateMover9001: ")
    for dq in crates:
        print(dq[-1], end=" ")

    return crates


if __name__ == "__main__":
    path = "data/day5.txt"
    ### part 1
    crates, instructions = readData(path)
    part1 = moveCrates(crates, instructions)

    ### part 2
    crates2, instructions2 = readData(path)
    part2 = crateMover9001(crates2, instructions2)
