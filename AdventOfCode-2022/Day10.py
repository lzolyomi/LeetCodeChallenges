#############################################
############ Advent of Code 2022 ############
################# Day 10 ####################
#############################################


def run_operations(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    x = 1  # initial value of register
    for l in data.splitlines():
        yield x  # regardless of line, one cycle passes, return value of register
        if l != "noop":  # if instruction passed
            yield x  # second cycle passes
            x += int(l.split(" ")[-1])  # after second cycle, modify register


def part_1(path: str):
    cycle_checks = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    for cycle, x in enumerate(run_operations(path)):
        if cycle + 1 in cycle_checks:
            signal_strength += x * (cycle + 1)
    print(f"### Result for part1: {signal_strength}")
    return signal_strength


def part_2(input_file: str, width: int = 40):
    rows = []
    row_string = ""
    for cycle, x in enumerate(run_operations(input_file)):
        horizontal_pos = cycle % width
        #           get horizontal pos with cycle
        crt_active = abs(horizontal_pos - x) < 2
        #      if diff. between hpos and register < 2
        #      means that cycle is in 'active' zone of CRT (activated by register +-1)
        if crt_active:
            row_string += "#"
        else:
            row_string += "."
        if (cycle + 1) % width == 0:
            # start new row
            rows.append(row_string)
            row_string = ""

    for row in rows:
        # print screen of CRT
        print(row)


if __name__ == "__main__":
    path = "data/day10.txt"
    part_1(path)
    part_2(path)
