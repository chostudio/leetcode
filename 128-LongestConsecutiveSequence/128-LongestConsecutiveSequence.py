# Last updated: 9/11/2025, 12:32:31 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aset = set(nums)
        count = 0
        for number in aset:
            # only when prev number not in set bc that means we'll count this number in another consecutive while loop
            if number - 1 not in aset:
                temp = 0
                while number + temp in aset:
                    temp += 1
                count = max(count, temp)
        return count