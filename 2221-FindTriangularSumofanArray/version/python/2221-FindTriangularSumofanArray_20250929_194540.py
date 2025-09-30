# Last updated: 9/29/2025, 7:45:40 PM
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        stack = [nums]
        while len(stack[-1]) != 1:
            temp = []
            arr = stack[-1]
            for i in range(len(arr)-1):
                val = (arr[i] + arr[i+1]) % 10
                temp.append(val)
            stack[-1] = temp
        return stack[-1][0]