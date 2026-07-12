# Last updated: 7/12/2026, 9:55:32 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        # a deque that acts as a queue. you push in from right, remove anything lesser than it, leftmost thing is biggest. if leftmost OOB then remove. store index in the deque, retrieve values with it from og array
4
5        ans = []
6
7        q = deque()
8
9        for i in range(len(nums)):
10            while q and nums[q[-1]] <= nums[i]:
11                q.pop()
12            q.append(i)
13            if q[0] <= i - k:
14                q.popleft()
15            if i >= k - 1: # obv dont jus start appending when fullk width hasnt happened
16                ans.append(nums[q[0]])
17
18
19        return ans