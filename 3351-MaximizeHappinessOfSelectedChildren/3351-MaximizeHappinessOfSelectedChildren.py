# Last updated: 9/11/2025, 12:30:24 PM
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        for i in range(k):
            if happiness[len(happiness)-i-1] - i > 0:
                res += happiness[len(happiness)-i-1] - i
        return res
    
#         res = 0
#         for i in range(k):
#             biggest = 0
#             index = 0
#             #find the biggest number in array
#             for j in range(len(happiness)):
#                 if happiness[j] > biggest:
#                     biggest = happiness[j]
#                     index = j
                
#                 if happiness[j] != 0:
#                     happiness[j] -= 1
#             res += biggest
#             #get rid of biggest number
#             happiness[index] = 0

#         return res