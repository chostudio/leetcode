# Last updated: 6/20/2026, 7:45:52 PM
1class Solution:
2    def countValidSubarrays(self, nums: list[int], x: int) -> int:
3        x = str(x)
4        count = 0
5        currsum = 0
6        for i in range(len(nums)):
7            currsum = 0
8            for j in range(i, len(nums)):
9                currsum += nums[j]
10                string = str(currsum)
11                if string[0] == string[-1] == x:
12                    count += 1
13        return count
14        
15        # prefix sum hashmap
16
17        arr = [0] * len(nums)
18        running = 0
19        for i in range(len(nums)):
20            running += nums[i]
21            arr[i] = running
22
23
24        # could sliding window be the correct solution? no theres no way to optimize it you have to try every combo sum
25            