# Last updated: 10/1/2025, 4:11:49 PM
from collections import defaultdict
import random

class RandomizedSet:

    def __init__(self):
        self.cache = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.cache:
            index = len(self.arr)
            self.arr.append(val)
            # what if we are not guarenteed to have unique values?
            self.cache[val] = index
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.cache:
            index = self.cache[val]
            
            self.cache[self.arr[-1]] = index
            self.arr[index] = self.arr[-1]
            del self.cache[val]
            self.arr.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        # messed up on random.randint it's [inclusive, inclusive]
        index = random.randint(0, len(self.arr)-1)
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()