# Last updated: 4/18/2026, 8:45:00 PM
1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        # for i in range(len(nums)):
4        #     left = max(nums[0:i+1])
5        #     right = min(nums[i:len(nums)])
6        #     if left - right <= k:
7        #         return i
8        # return -1
9
10
11        
12        # min and max stacks maybe
13        mini = []
14        maxi = []
15        length = len(nums)
16        for i in range(len(nums)):
17            if not maxi or maxi[-1] < nums[i]:
18                maxi.append(nums[i])
19            else:
20                maxi.append(maxi[-1])
21
22
23            if not mini or mini[-1] > nums[length-i-1]:
24                mini.append(nums[length-i-1])
25            else:
26                mini.append(mini[-1])
27
28
29        
30        mini.reverse()
31        for i in range(len(nums)):
32            if maxi[i] - mini[i] <= k:
33                return i
34
35        return -1