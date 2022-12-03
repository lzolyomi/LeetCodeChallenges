#############################################
############ Advent of Code 2022 ############
################# Day 2 #####################
#############################################
from typing import List


def readData(path: str) -> List:
    data = []  #
    with open(path, "r") as f:
        for l in f.readlines():  # for each line
            data.append((l[0], l[2]))

    for pair in data:
        assert len(pair) == 2, "There is a mismatch in tuple sizes!!"
    return data


#### First part ####
def assessStrategy(data):
    """Assess the assumed strategy the elf gave us by summarizing the total score in all rounds

    Args:
        data (iterable): the data read from the .txt file

    Returns:
        int: total score over all rounds
    """
    opponent_moves = {"A": "rock", "B": "paper", "C": "scissors"}
    own_moves = {"X": "rock", "Y": "paper", "Z": "scissors"}
    shape_scores = {"rock": 1, "paper": 2, "scissors": 3}

    ### Store rules as adjacency list like 'rock' defeats 'scissors' would be ('rock', 'scissors')
    rules = (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"))

    ### Iterate over all games
    score_counter = 0
    for opponent, own in data:
        opp_move = opponent_moves[opponent]
        own_move = own_moves[own]
        score = shape_scores[own_move]  ### keep track of score
        if opp_move == own_move:
            score += 3
        else:
            if (own_move, opp_move) in rules:
                score += 6
            elif (opp_move, own_move) in rules:
                pass
            else:
                raise ValueError("No one wins but its not draw")
        score_counter += score

    return score_counter


def correctStrategy(data):
    opponent_moves = {"A": "rock", "B": "paper", "C": "scissors"}
    shape_scores = {"rock": 1, "paper": 2, "scissors": 3}

    ### Store rules as adjacency list like 'rock' defeats 'scissors' would be ('rock', 'scissors')
    rules = (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"))
    activity_map = {"X": "lose", "Y": "draw", "Z": "win"}
    score_count = 0
    for opponent, activity in data:
        score = 0
        opp_move = opponent_moves[opponent]
        my_activity = activity_map[activity]
        my_shape = None  # stores what I should be showing
        if my_activity == "draw":
            my_shape = opp_move
            score += 3
        elif my_activity == "lose":
            for win, lose in rules:
                if win == opp_move:
                    my_shape = lose
        elif my_activity == "win":
            score += 6
            for win, lose in rules:
                if lose == opp_move:
                    my_shape = win

        score += shape_scores[my_shape]
        score_count += score

    return score_count


if __name__ == "__main__":
    path = "data/day2.txt"
    data = readData(path)
    part1 = assessStrategy(data)
    part2 = correctStrategy(data)
    print(f"Final result of part 1: {part1}")
    print(f"Final result of part 2: {part2}")
