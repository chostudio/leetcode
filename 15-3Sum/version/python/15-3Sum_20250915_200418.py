# Last updated: 9/15/2025, 8:04:18 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break # impossible to hit 0 if all positive

            # MUST HAVE CASE WHERE NO DUPLICATES FOR i HERE
            if i != 0 and nums[i] == nums[i-1]: # dont check on 0th index bc no numbers before that one
                continue # move onto next number
            l = i + 1
            r = len(nums) -1
            while l < r:
                amount = nums[i] + nums[l] + nums[r]
                if amount > 0:
                    r -= 1
                elif amount < 0:
                    l += 1
                elif amount == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1 # MUST INCREMENT BOTH BY ONE HERE

                    # continue but dont have duplicates. l - 1 is fine not OOBounds bc we did l = i + 1 before
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return ans
