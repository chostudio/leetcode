# Last updated: 11/4/2025, 9:34:16 AM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap plus q. heap to get largest task first. q to wait cooldown and then when the time of the next one is ready (bc they're all same time wait so FIFO queue) then popout and put back into heap
        heap = []
        taskmap = defaultdict(int)
        for t in tasks:
            taskmap[t] += 1
        
        for letter, freq in taskmap.items():
            heapq.heappush(heap, (-freq, letter))
        
        q = deque() # time, freq, letter
        time = 0
        while heap or q:
            time += 1
            if heap:
                freq, letter = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    q.append((time + n, freq, letter))
            if q and q[0][0] <= time:
                t, freq, letter = q.popleft()
                heapq.heappush(heap, (freq, letter))
            # put back in
            
        return time