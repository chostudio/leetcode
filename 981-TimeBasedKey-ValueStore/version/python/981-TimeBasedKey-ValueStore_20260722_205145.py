# Last updated: 7/22/2026, 8:51:45 PM
1class TimeMap:
2
3    def __init__(self):
4        # so instead of having snapshots of the entire array (bc some vals wont change) it's more efificent to store keys and when the values change within a key then only need to update that key
5        # value: [(time, value)] then bin search on values
6        self.vals = defaultdict(list)
7
8    def set(self, key: str, value: str, timestamp: int) -> None:
9        # we are assuming that these times will be in order, otherwise j sort them
10        self.vals[key].append((timestamp, value))
11        
12
13    def get(self, key: str, timestamp: int) -> str:
14        
15        if key not in self.vals:
16            return ""
17
18        # biggest timestamp
19        l, r = 0, len(self.vals[key]) -1
20        ans = ""
21        besttime = -1
22        while l <= r:
23            mid = (l + r) //2
24            print(self.vals[key][mid])
25            time, val = self.vals[key][mid]
26            # you need to store both answer STRING and besttime INT
27            if time <= timestamp:
28                if time > besttime:
29                    besttime = time
30                    ans = val
31                l = mid + 1
32            else:
33                r = mid - 1
34        return ans
35
36
37# Your TimeMap object will be instantiated and called as such:
38# obj = TimeMap()
39# obj.set(key,value,timestamp)
40# param_2 = obj.get(key,timestamp)