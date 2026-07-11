# Last updated: 7/11/2026, 12:31:04 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        boats = 0
5        Left = 0
6        Right = len(people)-1
7        # 2, 1
8        # boats = 3
9        while Left <= Right:
10            biggest = people[Right] # 3
11            smallest = people[Left] # 2
12            if biggest == limit or biggest + smallest > limit:
13                Right -= 1
14                boats += 1
15                continue
16            Right -= 1
17            Left += 1
18            boats += 1
19        return boats
20