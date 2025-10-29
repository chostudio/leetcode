# Last updated: 10/28/2025, 10:38:17 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        third = len(nums) // 3
        count = Counter(nums)
        ans = []
        for key, val in count.items(): # ITEMS ITEMS ITEMS is both
        # print(key, val)
            if val > third:
                ans.append(key)
        return ans