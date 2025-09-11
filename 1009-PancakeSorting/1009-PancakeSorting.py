# Last updated: 9/11/2025, 12:31:23 PM
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr), 1, -1):
            # find max index, which will be within the range arr.length()
            index = arr.index(i)
            # add to answer before editing arr
            ans.append(index+1)
            ans.append(i)
            # reverse first part and remove anything after that's already sorted
            arr = arr[:index:-1] + arr[:index]
        return ans