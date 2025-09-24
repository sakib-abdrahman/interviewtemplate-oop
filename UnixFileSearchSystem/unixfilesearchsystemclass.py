# Unix File Search System (Frequency: 4 / 5)
# Problem: Create a search API that can search through a file system for files matching certain filters (by name, size, extension).
# Concepts: Tree traversal, filtering strategy

from abc import ABC, abstractmethod
from collections import deque
from typing import List
from enum import Enum

# File
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.is_directory = False if '.' in name else True
        self.children = []
        self.extension = name.split(".")[1] if '.' in name else ""

    def __repr__(self):
        return "{"+self.name+"}"

# Filters
class Filter(ABC):  # interface
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, file):
        pass

class MinSizeFilter(Filter):  # concrete class
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size > self.size

class ExtensionFilter(Filter):
    def __init__(self, extension):  # "txt"
        self.extension = extension

    def apply(self, file):
        return file.extension == self.extension

# LinuxFindCommand
class LinuxFind():
    def __init__(self):
        self.filters: List[Filter] = []

    def add_filter(self, given_filter):
        # validate given_filter is a filter
        if isinstance(given_filter, Filter):
            self.filters.append(given_filter)

    def apply_OR_filtering(self, root):
        # f1 = File("root_300", 300)
        found_files = []
        # bfs
        queue = deque()
        queue.append(root)
        while queue:
            # print(queue)
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                for filter in self.filters:
                    if filter.apply(curr_root):
                        found_files.append(curr_root)
                        print(curr_root)
                        break
        return found_files

    def apply_AND_filtering(self, root):
        found_files = []
        # bfs
        queue = deque()
        queue.append(root)
        while queue:
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                is_valid = True
                for filter in self.filters:
                    if not filter.apply(curr_root):
                        is_valid = False
                        break
                if is_valid:
                    found_files.append(curr_root)
                    print(curr_root)
        return found_files


# Example usage
if __name__ == "__main__":
    f1 = File("root_300", 300)
    f2 = File("fiction_100", 100)
    f3 = File("action_100", 100)
    f4 = File("comedy_100", 100)
    f1.children = [f2, f3, f4]

    f5 = File("StarTrek_4.txt", 4)
    f6 = File("StarWars_10.xml", 10)
    f7 = File("JusticeLeague_15.txt", 15)
    f8 = File("Spock_1.jpg", 1)
    f2.children = [f5, f6, f7, f8]

    f9 = File("IronMan_9.txt", 9)
    f10 = File("MissionImpossible_10.rar", 10)
    f11 = File("TheLordOfRings_3.zip", 3)
    f3.children = [f9, f10, f11]

    f11 = File("BigBangTheory_4.txt", 4)
    f12 = File("AmericanPie_6.mp3", 6)
    f4.children = [f11, f12]

    greater5_filter = MinSizeFilter(5)
    txt_filter = ExtensionFilter("txt")

    my_linux_find = LinuxFind()
    my_linux_find.add_filter(greater5_filter)
    my_linux_find.add_filter(txt_filter)

    print("OR filtering results:")
    print(my_linux_find.apply_OR_filtering(f1))

    print("\nAND filtering results:")
    print(my_linux_find.apply_AND_filtering(f1))