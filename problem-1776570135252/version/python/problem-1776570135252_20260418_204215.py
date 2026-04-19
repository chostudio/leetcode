# Last updated: 4/18/2026, 8:42:15 PM
1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3
4
5        for i in range(len(nums)):
6            left = max(nums[0:i+1])
7            right = min(nums[i:len(nums)])
8            if left - right <= k:
9                return i
10        return -1
11
12
13        
14        # min and max stacks maybe
15        smallest = inf
16        mini = []
17        maxi = []
18        for i in range(len(nums)):
19            if not maxi or maxi[-1] < nums[i]:
20                maxi.append(nums[i])
21            else:
22                maxi.append(maxi[-1])
23
24
25            if not mini or mini[-1] > nums[i]:
26                mini.append(nums[i])
27            else:
28                mini.append(mini[-1])
29
30
31        
32            smallest = min(smallest, maxi[-1] - mini[-1])
33
34        return -1 if smallest == inf else smallest