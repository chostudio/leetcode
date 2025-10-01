# Last updated: 10/1/2025, 11:12:52 AM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # three sum but you have a result variable that keeps track of the absolute difference and you want the smallest one either the curr one or the new one compared the target nunmber. then you assign the sum of the three intergers to them.
        nums.sort()
        ans = sum(nums[:3]) # guarenteed to have at least 3 values
        for i in range(len(nums)-2):
            # i + 1 bruh not 0 remember
            l, r = i + 1, len(nums)-1
            while l < r:
                output = nums[i] + nums[l] + nums[r]
                if abs(output-target) < abs(ans-target):
                    ans = output # update with new sum
                elif output > target:
                    r -= 1
                else:
                    l += 1
        return ans