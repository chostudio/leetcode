# Last updated: 5/20/2026, 3:08:22 PM
1class Solution:
2    def splitArray(self, nums: List[int], k: int) -> int:
3        
4        # its contigious
5        def check(largestsum):
6            curramount = 0
7            subarraycount = 1
8            for i in nums:
9                if curramount + i > largestsum:
10                    subarraycount += 1
11                    curramount = 0
12                curramount += i
13            return subarraycount
14        
15        # smallest case is just the biggest number over and over again.
16        # biggest case is all nums sum? any better way to do this?
17        l, r = max(nums), sum(nums)
18        ans = inf
19        while l <= r: # must have this be equal because we want to check up to the last possible value
20            midsubarrval = (l + r) // 2
21            splits = check(midsubarrval)
22            if splits <= k: # valid split, this number works
23                ans = min(ans, midsubarrval) # remember that its not the amount of splits we want, but rather the min max val per thing which is midsubarrval
24                # lets go smaller and risk it
25                r = midsubarrval - 1
26                # okay here's the crazy part, it doesnt need to be exactly k subarrays. if it's less, then we still count it as a valid answer bc i guess technically we would keep going anywayas probably
27
28                # elif splits < k: # we must have k subarrays, thus that means our value per subarray is too high:
29                # r = midsubarrval - 1
30            else: # greater, does not work
31                l = midsubarrval + 1
32        print(ans)
33        return ans
34            