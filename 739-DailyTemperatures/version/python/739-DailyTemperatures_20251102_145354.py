# Last updated: 11/2/2025, 2:53:54 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # one pass
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                ptempval, pindex = stack.pop()
                ans[pindex] = i - pindex
            stack.append((temperatures[i], i))
        return ans