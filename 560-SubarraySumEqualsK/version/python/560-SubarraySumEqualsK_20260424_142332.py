# Last updated: 4/24/2026, 2:23:32 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        # lovely lovely prefix sum
4        # omg you can two sum this one
5        seen = defaultdict(int)
6        ans = 0
7        prefixsum = 0
8        for val in nums:
9            prefixsum += val
10            if prefixsum == k:
11                ans +=1 
12            if prefixsum - k in seen:
13                ans += seen[prefixsum - k]
14            
15            seen[prefixsum] += 1
16        return ans
17
18
19
20