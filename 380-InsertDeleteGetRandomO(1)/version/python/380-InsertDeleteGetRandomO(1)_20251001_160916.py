# Last updated: 10/1/2025, 4:09:16 PM
class RandomizedSet:

    def __init__(self):
        self.hashmap = collections.defaultdict(int) # values & index
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        # assuming we are guarenteed to only have one of each value/values are unique. otherwise we would have set of indicies instead of just one
        self.hashmap[val] = len(self.arr)
        self.arr.append(val) # need to do this one after bc the starting one needs to be index 0 
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False

        idx = self.hashmap[val]
        
        # for O(1) time, OVERWRITE with end position in arr to update to be deleted val index (not swap)
        self.arr[idx] = self.arr[-1]
        # update end val to deleted val index in hashmap
        self.hashmap[self.arr[-1]] = idx
        del self.hashmap[val]
        # val to be deleted is now last element so just pop for O(1) time
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.arr)-1)
        return self.arr[idx]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()