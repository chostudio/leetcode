# Last updated: 9/11/2025, 12:30:52 PM
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # just two pointer iterate through both. if more than 2 are not in the same place then false. problem says it's eqaul length strings. BUT also needs to make sure that the letters are available, can't swap to get a true if they dont even have the letters available in the first place
        # check for letter cout first with hashmap. they HAVE to have the same letter count in order for a successful swap to happen.
        hashmap = {}
        for i in range(len(s1)):
            hashmap[s1[i]] = hashmap.get(s1[i], 0) + 1
            hashmap[s2[i]] = hashmap.get(s2[i], 0) - 1
        count = 0
        for i in hashmap.values():
            if i != 0:
                return False

        differ = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differ += 1
        return False if differ > 2 else True
        