#############################################
############ Advent of Code 2022 ############
################# Day 17 ####################
#############################################
# thanks to @hugseverycat, his solution helped me a lot in coming up with mine
# link to his code: https://github.com/hugseverycat/aoc2022/blob/main/day17.py


class Rock:
    def __init__(self, shape, height):
        # all possible shapes in order of appearance
        # - :     + :  .#.  revL: ..#   | : #   square:
        #    ####      ###        ..#       #          ##
        #              .#.        ###       #          ##
        #                                   #
        #     ^         ^         ^         ^          ^
        #     1.        2.        3.        4.         5.
        if isinstance(shape, (int, float)):
            shape = self.possible_shapes[shape]
        assert shape in self.possible_shapes, "Invalid shape!!"
        assert height > 0, "Invalid (non-positive) height!"
        self.shape = shape
        ### Form of each shape
        if self.shape == "-":
            self.pos = set([(i + 2, height) for i in range(4)])
        elif self.shape == "+":
            self.pos = set(
                [
                    (3, height),
                    (2, height + 1),
                    (3, height + 1),
                    (4, height + 1),
                    (3, height + 2),
                ]
            )
        elif self.shape == "revL":
            self.pos = set(
                [
                    (4, height + 1),
                    (4, height + 2),
                ]
                + [(i + 2, height) for i in range(3)]
            )
        elif self.shape == "|":
            self.pos = set([(2, i) for i in range(height, height + 4)])
        elif self.shape == "square":
            self.pos = set([(2, height), (2, height + 1), (3, height), (3, height + 1)])

        assert len(self.pos) > 0, "No positional coordinates for Rock!"

    def __repr__(self):
        return f"Rock {self.shape}, num coords: {len(self.pos)}"

    @property
    def possible_shapes(self):
        return ["-", "+", "revL", "|", "square"]

    def move_down(self, tetris):
        """Moves the rock down one step.
        If it collides with any rock in the board, the movement is reverted

        Args:
           tetris (Tetris): Tetris object

        Returns:
            bool: True if movement successful (Rock.pos updated),
                  False if movement collides with rocks (Rock.pos remain the same)
        """
        # new hypothethical coordinates with y axis decreased once
        new_coords = set([(x, y - 1) for x, y in self.pos])
        # if new coords contains any elements from the game board
        # it means that it would overlap with a rock already in place
        # hence, movement is not possible
        if new_coords.intersection(tetris.game_board):
            # return False in case movement not possible
            # note that self.pos remains unchanged
            return False
        # check if all y coordinates are still above playing field (above zero)
        elif any([y < 0 for _, y in new_coords]):
            return False
        # in case movement possible, update to new coordinates
        self.pos = new_coords
        # return True to signal movement completed
        return True

    def move_side(self, direction: str, tetris):
        """Moves the rock sideways one step.
        If it collides with any rock or the edge of the board, the movement is not performed

        Args:
            direction (str): either < or > to signal the direction of the movement
            tetris (Tetris): the Tetris object, containing the current state of the board
        """
        assert direction in [">", "<"], "Invalid direction!"
        if direction == ">":  # we go right
            new_coords = set([(x + 1, y) for x, y in self.pos])
            if all([x in tetris.border for x, _ in new_coords]):
                # movement is not on the edge
                if not new_coords.intersection(tetris.game_board):
                    # if new position does not intersect with any new rock
                    # update its position
                    self.pos = new_coords
        elif direction == "<":  # we go left
            new_coords = set([(x - 1, y) for x, y in self.pos])
            if all([x in tetris.border for x, _ in new_coords]):
                # movement is not on the edge
                if not new_coords.intersection(tetris.game_board):
                    # if new position does not intersect with any new rock
                    # update its position
                    self.pos = new_coords


class Tetris:
    def __init__(self, path: str, width: int = 7):
        #### READ AND PARSE INPUT SEQUENCE ####
        with open(path, "r") as f:
            self.directions = f.readline().strip()
        print(
            f"Gas stream directions initialized, total of {len(self.directions)} items"
        )
        #### INITIALIZE TETRIS GAME ####
        # store height of each column
        self.height = {i: 0 for i in range(width)}
        # borders of the game. x coord cannot exceed these borders
        self.border = range(0, width)
        ### PART 2 modifications:
        # Use a state dictionary to keep track of the number of rocks
        self.states = dict()
        # Initialize jet (string) index
        self.jet_index = 0
        # Initialize the game board as an empty set
        self.game_board = set()

    @property
    def max_height(self):
        return max([x for x in self.height.values()])

    @property
    def relative_tower_height(self):
        """Returns a tuple with relative tower heights
        (relative to smallest element)

        Returns:
            tuple: relative height of each tower
        """
        smallest = min([x for x in self.height.values()])
        return tuple([x - smallest for x in self.height.values()])

    def single_rock(self, shape):
        """Simulates the fall of a single rock at the current board position.
        After the rock came to rest updates the board position.

        Args:
            shape (int): which type of rock should fall
        returns: tuple with the state (relative_height, rock_shape, jet_index)
        """
        rock = Rock(shape, self.max_height + 3)
        # moving := track if rock is still falling
        moving = True
        while moving:
            # as long as rock moves
            # move horizontally once
            # NOTE: does not matter if actually executed or not
            jet_direction = self.directions[self.jet_index]
            rock.move_side(jet_direction, self)
            self.jet_index += 1  # increase jet index
            if self.jet_index >= len(self.directions):
                self.jet_index = 0
            # let rock move down. fall:= True if rock fell, False if obstructed
            fall = rock.move_down(self)
            if not fall:  # if cannot fall, stop rock
                moving = False

        # add the rock came to rest to the game board
        self.game_board.update(rock.pos)
        for x, y in rock.pos:
            # update self.height with highest elements
            self.height[x] = max(self.height[x], y + 1)
        return tuple([self.relative_tower_height, shape, self.jet_index])

    def play_game(
        self,
        rounds: int,
        shape_index: int = 0,
    ):
        """Play the tetris game with the given rules

        Args:
            rounds (int): number of rounds to play (2022 in part 1)
            game_board (set): option to pass an existing game board position and continue playing that
                            Defaults to empty set (empty board)
            jet_index (int): index of the string containing the jet stream directions to start from
                            Defaults to zero (beginning of the string)
            shape_index (int): index of the rock shape to start from
                            Defaults to zero (beginning of the string)
        """
        ### Reset the game_board position to argument passed
        # or initialize an empty game
        ### Indices, intialized as (default) function arguments
        # shape_index = 0  # index used to access shape
        # jet_index = 0
        cycle_found = False
        roun = 0
        added_height = 0  # if no cycle found, returns zero
        while roun < rounds:
            # for roun in range(1, rounds + 1):
            roun += 1
            assert self.jet_index in range(
                len(self.directions)
            ), "Jet direction index invalid!"
            # read the next direction in the jetstream
            if shape_index > 4:  # restart shapes from beginning
                shape_index = 0
            # init new rock with given shape and 3 levels above max height
            # then place in the corresponding place
            state = self.single_rock(shape_index)
            shape_index += 1
            #### Modifications for Part 2
            if not cycle_found:
                if state not in self.states:  # no cycle found yet
                    self.states[state] = tuple([roun, self.max_height])

                else:  # CYCLE FOUND
                    cycle_found = True
                    print(f"Cycle found at round {roun}")
                    # Get last seen rocks and height from state
                    num_rocks, height = self.states[state]
                    # How many rocks in one cycle
                    cycle_rock_count = roun - num_rocks
                    # How much height a cycle adds
                    cycle_height = self.max_height - height
                    # How many rocks remain AFTER DETECTING CYCLE
                    rem_rocks = rounds - roun
                    # How many more cycles will fit in the remaining needed rocks
                    rem_cycles = rem_rocks // cycle_rock_count
                    # how many tocks to put down after all full cycles
                    rocks_to_put = rem_rocks % cycle_rock_count

                    ### Calculate height increase from all cycles
                    added_height = rem_cycles * cycle_height
                    roun = rounds - rocks_to_put

            # else:
            #     print(f"AFTER CYCLE DETECTION, ROUND {roun}")
        return int(self.max_height + added_height)


if __name__ == "__main__":
    path = "data/day17.txt"
    tetris = Tetris(path)
    part1 = tetris.play_game(2022)
    print(f"Solution to part 1: {part1}")
    tetris2 = Tetris(path)
    part2 = tetris2.play_game(1_000_000_000_000)
    print(f"Solution to part 2: {part2}")
