# Last updated: 5/19/2026, 10:35:55 AM
1class Solution:
2    def minJumps(self, arr: List[int]) -> int:
3        
4        adj = defaultdict(list)
5        for index, val in enumerate(arr):
6            adj[val].append(index)
7            # value 100 is at indicies 1,2,3 ex.
8        
9        if len(arr) == 1:
10            return 0
11        q = deque([0])
12        moves = 0
13        visited = set([0])
14        while q:
15            level = len(q)
16            # dont need temp array unless you're going to edi tit
17            for i in range(level):
18                index = q.popleft()
19                for nei in adj[arr[index]]:
20                    if nei != index and nei not in visited:
21                        if nei == len(arr) - 1:
22                            return moves + 1
23                        q.append(nei)
24                        visited.add(nei) # want to tell tother nodes that we're visitng it
25                # and when you delete it you need to access the hashmap value and just del instead of assigning an empty array
26                del adj[arr[index]] # we need to clear the adj list. bc technically, we dont need to itertae through the same value twice bc we would already have queued up all the possible jumps on the first time we access it. worst case is array has all same values, which would make this O(n^2), so we must clear it after first use
27                # or if not by value, then just move it
28                if index - 1 >= 0 and index - 1 not in visited:
29                    q.append(index - 1)
30                    visited.add(index - 1)
31                if index + 1 == len(arr) - 1:
32                    return moves + 1
33                if index + 1 < len(arr) -1 and index + 1 not in visited:
34                    q.append(index + 1)
35                    visited.add(index + 1)
36            moves += 1
37        # dont need to return anything here because it should be possible in worst case scenario to reach end of array by incrementing by 1 every time
38        return len(arr)