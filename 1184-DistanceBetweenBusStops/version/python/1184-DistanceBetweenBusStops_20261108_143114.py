# Last updated: 11/8/2026, 2:31:14 PM
1class Solution:
2    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
3        
4        if start == destination:
5            return 0
6        shortest = 10 ** 10 # didnt have it high enough lol
7        i = start
8        amount = 0
9        while i != destination:
10            amount += distance[i]
11            i += 1
12            if i >= len(distance):
13                i = 0
14        
15        shortest = min(shortest, amount)
16        i = start
17        amount = 0
18        while i != destination:
19            # in backwards the cost is i-1 so we decrement first
20            i -= 1
21            amount += distance[i]
22            if i < 0:
23                i = len(distance) - 1
24        shortest = min(shortest, amount)
25
26        return shortest
27        # two vars. one is keep on increasing, other is keep on decreasing. if you hit the end for either, then keep on going from the other end. Note that it's not first the hit at BFS. It is actually Dijkstra weights. so you could do queue or non something.
28
29        # actually its just two for loops both directions of array