# Last updated: 9/29/2025, 8:45:39 AM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonitc stack, two whilel oops lets see if you remember it
        stack = []
        ans = [0 for x in range(len(temperatures))]
        for i in range(len(temperatures)):
            # store as a 2d arr where one is val, second is index
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                temp, index = stack.pop()
                ans[index] = i - index
            stack.append([temperatures[i], i])
        return ans