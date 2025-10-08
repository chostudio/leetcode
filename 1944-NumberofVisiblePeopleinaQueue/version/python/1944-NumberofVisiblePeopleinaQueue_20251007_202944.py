# Last updated: 10/7/2025, 8:29:44 PM
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        Stack = [] # [ 10, 3, 2, 1
        Res = [] # [0, 1, 1, 1
        Count = 0 # 1
        for i in range(len(heights)-1,-1, -1):
            Count = 0
            while len(Stack) != 0 and heights[i] > Stack[-1]:
                Stack.pop()
                Count += 1
            if len(Stack) != 0:
                Count += 1
            Stack.append(heights[i])
            Res.append(Count)
        Res.reverse()
        return Res
