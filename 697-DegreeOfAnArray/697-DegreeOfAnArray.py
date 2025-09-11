# Last updated: 9/11/2025, 12:31:34 PM
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(list)
        defaultdict()
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]].append(1)
                count[nums[i]].append(i)
                count[nums[i]].append(i)
            else:
                count[nums[i]][0] += 1
                count[nums[i]][2] = i
        minLength = 0
        numCount = 0
        for key, val in count.items():
            if count[key][0] > numCount:
                numCount = count[key][0]
                minLength = count[key][2] - count[key][1]
            elif count[key][0] == numCount: 
                if count[key][2] - count[key][1] < minLength:
                    numCount = count[key][0]
                    minLength = count[key][2] - count[key][1]
        return minLength + 1
