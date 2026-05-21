# Last updated: 5/21/2026, 11:10:46 AM
1class Solution:
2    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
3        s = set()
4        for num in arr1:
5            temp = num
6            while temp > 0:
7                s.add(temp)
8                temp //= 10 # pop off the last digit
9        
10        # to get longest need to keep track of max length O(arr2). this is better time complexity than sorting it. 
11        longest = 0
12        for num in arr2:
13            temp = num
14            while temp > 0:
15                # we want the longest of any two pairs
16                if temp in s:
17                    longest = max(longest, len(str(temp)))
18                    break # even if we go shorter within same word it will just be shorter
19                temp //= 10
20        return longest
21        