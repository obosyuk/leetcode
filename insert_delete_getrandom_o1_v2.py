import random


class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.list = list()

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            index = self.map[val]

            self.list[index], self.list[-1] = self.list[-1], self.list[index]
            self.map[self.list[index]] = index

            self.list.pop()
            del self.map[val]

            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)

