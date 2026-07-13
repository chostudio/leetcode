# Last updated: 7/12/2026, 5:51:56 PM
1class Solution:
2    def findMinDifference(self, timePoints: List[str]) -> int:
3        # conver to a standardiszed format e.g. minutes only, then interval sort and get adjacent ones basically. alteratively, since it's a 24 hours clock you can look through every minut but that would be less efficient if there are less times than every minute on this thing. if there are more times than every minute in a day, then yes it would be more efficient. reminder to check dist between smallest and biggest time bc wrap around proptyt is valid
4        # if any two points are the same, then it's 0 and just return right away. no need to has a hashmap for this, just do it in the interval honestly
5
6        times = []
7        for time in timePoints:
8            hour, mi = time.split(":")
9            calc = int(hour) * 60 + int(mi)
10            times.append(calc)
11        
12        times.sort()
13        smallest = inf
14        for i in range(1, len(times)):
15            if times[i] == times[i-1]:
16                return 0
17            smallest = min(smallest, times[i] - times[i-1])
18        
19        # check wrap around
20        smallest = min(smallest, abs(times[-1] - 1440) + times[0])
21
22        return smallest