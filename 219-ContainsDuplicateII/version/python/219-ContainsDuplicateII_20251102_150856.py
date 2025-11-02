# Last updated: 11/2/2025, 3:08:56 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap bc indivces matter
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            # abs val between the indicies not value
            if nums[i] in hashmap and abs(hashmap[nums[i]] - i) <= k:
                return True
            hashmap[nums[i]] = i
        return False