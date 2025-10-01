# Last updated: 10/1/2025, 10:40:13 AM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # worst case is brute for which is O(n4) 
        # most efifeint way is O(n^3) omg bruh. it's threesum but you shove it in another for loop exactly like the threesum one first. 
        nums.sort() # dont forget to sort it duhhhh
        ans = []
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i -1]:
                continue
            # inclusive, exclusive
            for j in range(i + 1, len(nums)-2):
                # why if j > i + 1? just not on the first iteration of j?
                if j > i + 1 and nums[j] == nums[j -1]:
                    continue
                l, r = j + 1, len(nums)-1
                while l < r:
                    output = nums[i] + nums[j] + nums[l] + nums[r]
                    if output == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]: # IT"S MINUS here not plus bc we dunno whats to the right of left but we know that left-1 wont be OOB bc the two loops before make it in bounds
                            l += 1
                        # in 4sum we need a second whlie loop for the right pointer to be decremented too. this is bc the number that stays the same is the first var "i", therefore the r pointer cannot be the one that is the same.
                        # while l < r and nums[r] == nums[r + 1]:
                        #     r -= 1
                    elif output < target:
                        l += 1
                    else: # output > target
                        r -= 1
        return ans
