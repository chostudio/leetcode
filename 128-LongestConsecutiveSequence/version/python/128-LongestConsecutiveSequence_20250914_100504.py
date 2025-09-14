# Last updated: 9/14/2025, 10:05:04 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # you just gotta turn into set then for loop loop
        aset = set(nums)
        longest = 0
        for i in aset:
            # you need a if statement here to not get a TLE. reason for this is we know the longest sequence won't be in the middle of a sequence aka if there's a number -1 value before the number then that means it's actually part of a longer sequence. to only get non overlapping sequences just always start the count from a started number with nothing before it
            if i - 1 not in aset:
                sequence = 1
                x = 1
                while i + x in aset:
                    sequence += 1
                    x += 1
                longest = max(longest, sequence)
        return longest