# Last updated: 5/21/2026, 11:20:21 AM
1class Solution:
2    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
3        # guarenteed that theres only 1 of each num in both arrays so we can just use a set bc it's 1-n. if freq amounts differed, then would use hashmap but set is fine here
4        s = set()
5        matches = 0 
6        ans = [0] * len(A)
7        for i in range(len(A)):
8            # check first then add to not count the same num
9            if A[i] in s:
10                matches += 1
11            if B[i] in s:
12                matches += 1
13            # edge case where if the two numbers are the same then we need to add them
14            # not +2, just +1 just like the others
15            if A[i] == B[i]:
16                matches += 1
17            ans[i] = matches
18            s.add(A[i])
19            s.add(B[i])
20        return ans