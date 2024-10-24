import random


class RandomizedSet:

    def __init__(self):
        self._options_dict = dict()

    def insert(self, val: int) -> bool:
        if val not in self._options_dict:
            self._options_dict[val] = None
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self._options_dict:
            del self._options_dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self._options_dict.keys()))

