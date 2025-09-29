# Last updated: 9/29/2025, 8:37:54 AM
class Solution:
    def check(self, nums: List[int]) -> bool:
        # you can use the trick here i think where you append two of the same. then i would start from the lowest value and make sure there's less then or equal to two "drops?" + has to be increasing order except for less then or equal to two times
        nums = nums + nums
        prev = -inf
        lessthentwodrops = 0
        for i in nums:
            if i < prev:
                lessthentwodrops += 1
            prev = i
        return lessthentwodrops <= 2
