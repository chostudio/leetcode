# Last updated: 8/2/2026, 9:44:06 AM
1class Solution:
2    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
3        # simulation wise i see how to do it. but whats the trick to getting it faster than simulating it. some data structure? like segment tree? mb we only really care about the biggest number in a certain range rather than all numbers
4
5        # what in the world is a difference array well i guess you'll breifly learn about it. didn't see how prefix sum will be applicable to this Q tbh. so learn that too
6
7        # okay line sweep would actually work on this and instead of using a heap just put it inside a second aray and traverse through both at same time so O(m + n)
8
9        arr = [0] * len(nums)
10        for start, end in queries:
11            # if for whatever reason the query numbers are totally out of bounds then we would discard it
12            if start >= len(nums) or end < 0:
13                continue
14            # but if one half of the query is in bounds, then just set the OOB half to the edge either start or end whereever OOB is
15            
16            if start < 0: start = 0
17            # bc we just change our running variable with the vals at index
18            arr[start] -= 1
19            # if at end or beyond end then we actually dont set the end value bc its oob bc exclusive
20            if end >= len(nums) - 1:
21                continue
22            # else it's inclusive so it needs to end + 1
23            arr[end +1] += 1
24        
25        diff = 0
26        for i in range(len(nums)):
27            diff += arr[i]
28            # + here not - bc diff is negative and dont want double negative
29            if nums[i] + diff > 0:
30                return False # cannot all be 0
31            # else it's 0 or below so we good
32        return True