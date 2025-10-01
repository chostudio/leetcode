# Last updated: 9/30/2025, 9:10:27 PM
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = []
        for num in nums:
            arr.append(str(num))
        
        # str * 100000
        # "9" * 100000 = "9999999"
        # "90" * 100000 = "90909090"
        arr.sort(key=lambda x: x * 100000, reverse=True) # reverse not reversed

        # there is one case where if the entire array is just 0s, we need to return "0" instead of "00000"
        return ''.join(arr) if arr[0] != "0" else "0"