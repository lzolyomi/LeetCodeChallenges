#############################################
############ Advent of Code 2022 ############
################# Day 11 ####################
#############################################
import re
from tqdm import tqdm
from math import lcm


def parseInput(path):
    with open(path, "r") as f:
        for line in f.readlines():
            # breakpoint()
            line = line.strip()
            if re.findall(r"\bMonkey\b", line):
                # new monkey found, reset all attributes
                starting_items = []
                operation = None  # will be lambda function
                test = {"divisible_by": None, "if_true": None, "if_false": None}
                # divisible by this integer, if true throw to monkdeyId, if false throw to monkeyID
            elif "Starting" in line.split():
                starting_items = [int(x) for x in re.findall(r"\d+", line)]
            elif "Operation:" in line.split():
                operation = line.split("=")[-1].strip(" ")
            elif "Test:" in line.split():
                test["divisible_by"] = int(re.findall(r"\d+", line)[0])
            elif re.findall(r"\btrue\b", line):
                test["if_true"] = int(re.findall(r"\d+", line)[0])
            elif re.findall(r"\bfalse\b", line):
                test["if_false"] = int(re.findall(r"\d+", line)[0])
            else:
                # end of a monkey
                yield {
                    "starting_items": starting_items,
                    "operation": operation,
                    "test": test,
                }
    yield {
        "starting_items": starting_items,
        "operation": operation,
        "test": test,
    }


class Monkey:
    def __init__(self, id, monkey_data: dict):
        self.id = id
        self.starting_items = monkey_data.get("starting_items")
        self.operation = monkey_data.get("operation")
        self.test_divisible = monkey_data.get("test").get("divisible_by")
        self.test_if_true = monkey_data.get("test").get("if_true")
        self.test_if_false = monkey_data.get("test").get("if_false")
        self.inspect_counter = 0  # how many times this monkey inspected
        self.monkey_data = monkey_data

    def __str__(self):
        old = 2
        return f"""Monkey with ID: {self.id} and items: {self.starting_items} \n
                with the lambda operation tested at 2: {eval(self.operation)} \n
                and test: if divisible with {self.test_divisible}
                then pass to monkey: {self.test_if_true} 
                otherwise pass to: {self.test_if_false} \n"""

    def inspect_item(self, monkeys: dict, relief=3):
        """Inspects the first element in starting_items
        increases the worry level, according to operation
        gets bored, divide worry level by 3
        check condition and throw item to corresponding monkey

        monkeys: dictionary of monkey objects, used to pass the objects
        """
        old = self.starting_items.pop(0)
        new_worry_level = eval(self.operation)
        self.inspect_counter += 1  # monkey just inspected a new element
        if relief == 3:
            new_worry_level //= relief
        else:
            # divide with modulo test_level. it doesn't change the second modulo operator
            new_worry_level %= relief
        if new_worry_level % self.test_divisible == 0:
            monkeys[self.test_if_true].receive_item(new_worry_level)
        else:
            monkeys[self.test_if_false].receive_item(new_worry_level)

    def receive_item(self, item_worry_level):
        self.starting_items.append(item_worry_level)

    def has_items(self):
        return len(self.starting_items) > 0


def part1_main(path, iterations: int, relief=3):
    monkeys = {}  # stores monkey objects
    for id, m in enumerate(parseInput(path)):
        # populate monkey objects using generator
        monkeys[id] = Monkey(id, m)
    ### calculate largest common multiplier for part2
    if relief != 3:
        relief = lcm(*[m.test_divisible for _, m in monkeys.items()])

    ### play the rounds
    for _ in tqdm(range(iterations)):
        for key in range(max(monkeys.keys()) + 1):
            while monkeys[key].has_items():
                monkeys[key].inspect_item(monkeys, relief)
    inspect_counts = [m.inspect_counter for _, m in monkeys.items()]
    largest = max(inspect_counts)
    inspect_counts.remove(largest)
    second_largest = max(inspect_counts)
    print(inspect_counts)
    print(f"Two largest number multiplied: {largest*second_largest}")


if __name__ == "__main__":
    path = "data/day11.txt"
    part1_main(path, 20)
    part1_main(path, 10000, relief=1)
