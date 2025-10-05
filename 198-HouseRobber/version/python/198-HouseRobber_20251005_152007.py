# Last updated: 10/5/2025, 3:20:07 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        onehouseago = 0
        twohouseago = 0
        for house in nums:
            # to max it either we take the current house val + the house two ago OR we dont take the current val house bc the house one back is way more so we take that one
            curr = max(house + twohouseago, onehouseago)
            # shift it forward a house onto the next one
            twohouseago = onehouseago
            onehouseago = curr
        return onehouseago