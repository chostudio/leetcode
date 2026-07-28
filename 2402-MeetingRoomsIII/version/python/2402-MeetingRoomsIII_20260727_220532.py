# Last updated: 7/27/2026, 10:05:32 PM
1class Solution:
2    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
3        # truly, im just thinking heap simulation. maybe double heap. 1 for rooms avil, 1 for rooms taken, simulate by going +1 every for a time variable. maybe another heap for meetings. triple heap lowk possible. doable. + hashmap that keeps track of least used room and we O(n) loop through to get the ans.
4
5        meetlist = []
6        roomfreq = { x:0 for x in range(n)}
7        for start, end in meetings:
8            # min heap, smallest first
9            heapq.heappush(meetlist, (start, end))
10        
11        available = []
12        # you forgot to init by pushing all rooms into available
13        for room in range(n):
14            heapq.heappush(available, room)
15        taken = []
16        time = 0
17        while meetlist:
18            # first we want to see if any meetings ended
19            # syntax error taken[0] instead of taken[0][0]
20            while taken and taken[0][0] <= time:
21                endtime, roomnum = heapq.heappop(taken)
22                heapq.heappush(available, roomnum)
23
24            # note that there may be a case where if the meeting time has past then dont consider it. remove alr past meetings WE DONT cancel a meeting
25            # while meetlist and meetlist[0][1] <= time:
26            #     heapq.heappop(meetlist)
27
28            # then we want to fill up as many rooms we can with starting or ongoing meeting reservations
29            # 1. we have rooms 2. the meeting is starting (==) or past the start time and ready (room cleared up)
30            # smallest room popout first
31            # The delayed meeting should have the same duration as the original meeting.
32            while available and meetlist and time >= meetlist[0][0]:
33                roomnum = heapq.heappop(available)
34                meetstart, meetend = heapq.heappop(meetlist)
35                roomfreq[roomnum] += 1
36                newend = meetend if time == meetstart else time + abs(meetend-meetstart)
37                heapq.heappush(taken, (newend, roomnum))
38
39            # time += 1 # technically, we could probably jump to the next start point, but this works more realistically for now
40            # jump up to next start
41            if available: # room waiting for meeting, jump to next meeting start
42                time = max(time, meetlist[0][0] if meetlist else 0)
43            else:
44                # jump to the next time a room becomes available
45                time = taken[0][0]
46
47        # when all meetings have taken place (or are taking place) then we can check room
48        # held the most meetings (read the desc always)
49        biggestcount = -inf
50        ans = 0
51        for room, freq in roomfreq.items():
52            if freq > biggestcount:
53                biggestcount = freq
54                ans = room
55            elif freq == biggestcount and room < ans:
56                ans = room
57            
58        return ans