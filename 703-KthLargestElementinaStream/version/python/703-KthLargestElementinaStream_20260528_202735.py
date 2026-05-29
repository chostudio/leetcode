# Last updated: 5/28/2026, 8:27:35 PM
1class KthLargest:
2    # you forgot self.
3
4    def __init__(self, k: int, nums: List[int]):
5        self.heap = []
6        self.k = k
7        # YOU FORGOT TO DO THE NUMS HERE
8        for num in nums:
9
10            heapq.heappush(self.heap, num)
11            if len(self.heap) > k:
12                heapq.heappop(self.heap)
13
14    def add(self, val: int) -> int:
15        heapq.heappush(self.heap, val)
16        if len(self.heap) > self.k:
17            heapq.heappop(self.heap)
18        # we want the kth val. 
19        # min heap
20        return self.heap[0]
21
22
23# Your KthLargest object will be instantiated and called as such:
24# obj = KthLargest(k, nums)
25# param_1 = obj.add(val)