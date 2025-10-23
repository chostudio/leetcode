# Last updated: 10/23/2025, 11:40:56 AM
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        
        # guarenteed there willbe more than k queries
        heap = []
        # nearest obstacle for each query so 
        ans = []
        for x, y in queries:
            # max heap bc we want the kth nearest to origin so if we always have k values then the next value in the heap is the kth closest. everything in the kth/0th index will be smallest than it

            # dist is always positive so double negate bc max heap
            heapq.heappush(heap, (-abs(x)- abs(y))) # max heap on python is negated
            if len(heap) > k:
                heapq.heappop(heap)
                ans.append(-heap[0])
            elif len(heap) == k:
                ans.append(-heap[0])
            else:
                ans.append(-1)
            

        return ans