#############################################
############ Advent of Code 2022 ############
################# Day 7 #####################
#############################################


def readData(path: str) -> list:
    terminal_strings = []
    with open(path, "r") as f:

        for l in f.readlines():
            terminal_strings.append(l.strip("\n").split(" "))

    return terminal_strings


class File:
    def __init__(self, name, size):
        self.name = name
        if type(size) != int:  # cast string to integer before assign
            self.size = int(size)
        else:
            self.size = size


class Dir:
    def __init__(self, id, parent):
        self.parent = parent  # stores the parent Dir() object
        self.id = id  # full path of Directory
        self.directories = set()  # set of directories contained within this directory
        self.files = (
            set()
        )  # all the files that the Directory contains (mostly for debug purposes)

    @property
    def subdirectories(self):
        """Return a dictionary with subdirectory names and Dir objects"""
        return {d.id: d for d in self.directories}

    @property
    def filenames(self):
        """Return a dictionary with names of files as key, File object as value"""
        return {f.name: f for f in self.files}

    @property
    def total_size(self):
        """Total size of this directory. Sum of all files, plus sum of size of all subdirectories.
        Calculated by calling this function recursively
        """
        filesizes = sum([file.size for file in self.files])
        subdir_sizes = sum([d.total_size for d in self.directories])
        return filesizes + subdir_sizes

    def add_file(self, file):
        assert (
            file.name not in self.filenames
        ), "WARNING! This file has already been added to this Directory"
        self.files.add(file)  ## store filename in set

    def add_directory(self, dir):
        assert (
            dir.id not in self.subdirectories
        ), "WARNING! There is already a Directory added with this name to this object!"
        self.directories.add(dir)


class Terminal:
    def __init__(self):
        self.root = Dir("/", None)
        self.cwd = self.root

    def cd(self, path):
        if path == "..":
            if self.cwd == self.root:  ## cannot go up from root
                pass
            else:
                self.cwd = self.cwd.parent
        else:
            if path == "/":  # covering edge case for moving to root in the beginning
                pass
            else:
                self.cwd = self.cwd.subdirectories[path]

    def ls(self, file_split):
        """Call every time until we don't see another command

        Args:
            file_split (str): the line describing either a file or directory
        """
        if file_split[0] == "dir":  # if line represents a directory
            newdir = Dir(file_split[1], self.cwd)
            self.cwd.add_directory(newdir)

        else:  # if line represents a file
            newfile = File(file_split[1], file_split[0])
            self.cwd.add_file(newfile)

    @staticmethod
    def search_directory(root, n, smaller=True):
        """Given a Dir object, it will travel over all its children, appending each onto a list

        Args:
            root (Dir): root of directory structure
            n (int): Threshold under which to append
            smaller (bool): if True, will look for smaller than n sizes, if false, larger or equal to

        Returns:
            list: list of directories passing the criteria
        """
        if smaller:
            result = [root] if root.total_size <= n else []
        else:
            result = [root] if root.total_size >= n else []

        for subdir in root.directories:
            result += Terminal.search_directory(subdir, n, smaller)
        return result


def goOverTerminal(data):
    term = Terminal()
    ls_window = False
    for line in data:
        if line[0] == "$":  ## new command issued
            ls_window = False
            if line[1] == "cd":
                term.cd(line[2])
            elif line[1] == "ls":
                ls_window = True

        elif ls_window:
            term.ls(line)
    list_below_100k = [
        d.total_size for d in Terminal.search_directory(term.root, 100000)
    ]

    ### Answering part two
    total_space = 70000000
    unused_space = total_space - term.root.total_size
    space_needed = 30000000 - unused_space
    min_dir_size = [
        d.total_size for d in Terminal.search_directory(term.root, space_needed, False)
    ]
    print(f"Answer is: {sum(list_below_100k)} for PART 1")
    print(f"Answer is: {min(min_dir_size)} for PART 2")

    return term


if __name__ == "__main__":
    path = "data/day7.txt"
    data = readData(path)
    part1 = goOverTerminal(data)
