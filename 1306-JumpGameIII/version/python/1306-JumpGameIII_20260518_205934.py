# Last updated: 5/18/2026, 8:59:34 PM
1class Solution:
2    def canReach(self, arr: List[int], start: int) -> bool:
3        # one, check if there is a 0 in the array lol
4        iszero = False
5        i = 0
6        while i < len(arr):
7            if arr[i] == 0:
8                iszero = True
9                break
10            i += 1
11        if iszero is False: return False
12
13        # then bfs, least amount of jumps should reach the zero in shortest amount of jumps, else impossible
14        if arr[start] == 0: return True
15
16        # need a visited set to prevent infinite loop
17        visited = set()
18        q = deque([start])
19        while q:
20            index = q.popleft()
21            visited.add(index)
22            # first we check if inbounds, we cant go out of bounds.
23            if index - arr[index] >= 0:
24                # then we check if 0 off the bat, if it isnt then we add it
25                if arr[index - arr[index]] == 0:
26                    return True
27                if index - arr[index] not in visited:
28                    q.append(index - arr[index])
29            if index + arr[index] < len(arr):
30                if arr[index - arr[index]] == 0:
31                    return True
32                if index + arr[index] not in visited:
33                    q.append(index + arr[index])
34
35        return False