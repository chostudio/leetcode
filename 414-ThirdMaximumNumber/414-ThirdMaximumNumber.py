# Last updated: 9/11/2025, 12:31:50 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 3 variables, one loop. we do a trickle down kind of thing from one to two to two to three. if third var has nothing, then return max.
        #  or actually just check it against all three.
        # holy you almost had it you just needed to add the if statement to make sure to skip any duplicates
        biggest, second, third = None, None, None
        for i in nums:
            if i == biggest or i == second or i == third:
                continue
            if biggest is None or i > biggest:
                third = second
                second = biggest
                biggest = i
            elif second is None or i > second:
                third = second
                second = i
            elif third is None or i > third:
                third = i
        return biggest if third is None else third