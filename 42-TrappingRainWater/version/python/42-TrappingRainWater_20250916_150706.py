# Last updated: 9/16/2025, 3:07:06 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        lMax, rMax = height[left], height[right]
        while left <= right: # we want to get the last one where it intersects too
            if lMax > rMax:
                rMax = max(rMax, height[right])
                water += rMax - height[right]
                right -= 1
                
            else:
                lMax = max(lMax, height[left])
                water += lMax- height[left]
                left += 1
                
        return water
