#############################################
############ Advent of Code 2022 ############
################# Day 13 ####################
#############################################
import ast


def parse_data(path):
    list_pairs = []
    with open(path, "r") as f:
        pairs = []
        for line in f.readlines():
            if line != "\n":
                line_list = ast.literal_eval(line.strip())
                pairs.append(line_list)
            else:
                assert len(pairs) == 2, "PAIRS HAVE MORE/LESS elemenets"
                list_pairs.append(pairs)
                pairs = []
    if len(pairs) > 0:
        list_pairs.append(pairs)
    return list_pairs


def compare_pairs(l1, l2):
    """
    Idea is to cover all cases from the description and return:
    a positive number if the pairs are correctly ordered
    a negative number if pairs are incorrectly ordered
    0 if we have to continue with the evaluation (i.e. neutral)
    """
    match (l1, l2):
        case int(), int():
            return l2 - l1  # positive if second element higher
        case list(), list():  # both lists
            for item1, item2 in zip(
                l1, l2
            ):  # zip makes sure we only iterate until both lists have items
                result = compare_pairs(
                    item1, item2
                )  # recursively call compare on elements of list
                if (
                    result != 0
                ):  # 0 means no evaluation, any other number means we have a true/false outcome
                    return result
            return len(l2) - len(l1)  # if l2 larger this will be positive
        case int(), list():
            return compare_pairs(
                [l1], l2
            )  # recursively call compare on converted l1 and l2
        case list(), int():
            return compare_pairs(l1, [l2])


def part1(pairs):
    index_sum = 0  # sum of indices with correct pairs
    for i, pair in enumerate(pairs):
        assert len(pair) == 2, "LENGTH IS NOT 2"
        if compare_pairs(pair[0], pair[1]) > 0:
            index_sum += i + 1  # INDEXING STARTS AT 1!!!!
    print(f"Result for part 1: {index_sum}")
    return index_sum


def part2(pairs):
    # determine index of decoder packets
    indices = [1, 2]  # denote (initial) indices for [[2]] and [[6]]
    for i, pair in enumerate(pairs):
        for element in pair:
            # if element in pair is smaller than [[2]], increase index of [[2]]
            indices[0] += 1 if compare_pairs(element, [[2]]) > 0 else 0
            # if element in pair is smaller than [[6]], increase index of [[6]]
            indices[1] += 1 if compare_pairs(element, [[6]]) > 0 else 0

    print(f"Result for part2: {indices[0] * indices[1]}")


if __name__ == "__main__":
    path = "data/day13.txt"
    data_pairs = parse_data(path)
    part_1 = part1(data_pairs)
    part2(data_pairs)
