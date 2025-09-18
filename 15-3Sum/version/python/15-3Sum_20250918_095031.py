# Last updated: 9/18/2025, 9:50:31 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [] 
        nums.sort() # [-4, -1,-1, 0,1,2]

        for i in range(len(nums)): # 1
            if nums[i] > 0: # greataer than not equal to, [0,0,0] can be valid
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1 # 3, 4
            while l < r:
                sum = nums[i] + nums[l] + nums[r] # -1, 0, 1
                if sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1 # prevent not moving/stuck in loop by incrementing and decrementing
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum > 0:
                    r -= 1
                else: # smaller than zero
                    l += 1
        return ans

