# Last updated: 12/14/2025, 6:43:35 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        # reason this is bucket sort and not heap is bc 3*O(n) is asymp faster than nlogk
4        count = Counter(nums) # ez hashing trick counter
5        arr = [[] for i in range(len(nums) +1)] # have to do lambda instead of multiplcation trick
6
7        # put in 2d arr
8        # ITEMMMSSSMSSSS gets both key value
9        for val, freq in count.items():
10            # for val, freq in count.object():
11            arr[freq].append(val)
12        ans = [] # dont times by k just append bruh who cares
13        # iterate through it backwards
14        # no need to put k in side of a loop by itself just minus or plus it as we go
15        # reason of issue was off by one, since 1:1 would be in array slot 1 not 
16        for i in range(len(nums), 0, -1):
17            for val in arr[i]:
18                ans.append(val)
19                k -= 1
20                if k == 0: # just return instead of break
21                    return ans
22        