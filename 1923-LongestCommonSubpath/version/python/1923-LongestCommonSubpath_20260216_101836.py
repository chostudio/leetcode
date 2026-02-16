# Last updated: 2/16/2026, 10:18:36 AM
1class Solution:
2    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
3        
4        mod = (1 << 128) - 159
5        def rabin_karp(arr, window_size):
6            base = 1 << 17 # 17 not 10, bc 17 is a prime
7            # base power you need the mid value for the second one, it's not a number u make urself
8            base_power = pow(base, window_size - 1, mod)
9            rolling_window = 0 # this is our rolling/sliding window and the thing that we update to change. 
10            all_hashes = set() # this is what we return ( we want to return a set and we add in the rolling window snapshots into here)
11            # i have no idea what the equation is or the order of the overal thing, or what the numbers are supposed to be initialized at
12
13            # for every equation you need to wrap it in parenthesis and use % mod at the end
14            # timzing the rolling window by the base is only used in the initial window & middle step to shift the polynomial
15            
16            # to add the right most element, grab the element at the end of the window arr[start + window_size] and just add it
17
18            # add the first window into the thing
19            # yes you need to iterate through and use arr[i] duh
20            for i in range(window_size):
21                rolling_window = (rolling_window * base + arr[i]) % mod
22            # add the window
23            all_hashes.add(rolling_window)
24
25            # then shift window
26            for i in range(len(arr) - window_size):
27                # remove left, shift polynomial, add right, add into thing. We need to shift polynomial in middle bc thats what rolls it
28                # you only use times arr element by BASEPOWERin the "remove leftmost element" step (index at the start of the window). DO NOT base_power anywhere else
29                rolling_window = (rolling_window - arr[i] * base_power) % mod
30                rolling_window = (rolling_window * base) % mod
31                rolling_window = (rolling_window + arr[i+window_size]) % mod
32
33                all_hashes.add(rolling_window)
34            return all_hashes 
35
36        l, r = 0, min(len(p) for p in paths) + 1 # you have to plus one bc 0 index array
37        hashes = set()
38        while l + 1 < r:
39            mid = (l + r) // 2
40            hashes = [rabin_karp(p, mid) for p in paths]
41            overlaps = set.intersection(*hashes)
42            if len(overlaps) != 0:
43                l = mid
44            else:
45                r = mid
46        return l