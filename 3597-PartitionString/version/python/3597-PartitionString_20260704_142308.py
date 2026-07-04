# Last updated: 7/4/2026, 2:23:08 PM
1class Solution:
2    def partitionString(self, s: str) -> List[str]:
3        # note that in the first example, "ab" is not on considered a thing bc we move onto the next thing 
4        theset = set()
5        ans = []
6        # order matters so have both ans arr (answer) and set for checking O(1) time
7
8        curr = ""
9        for letter in s:
10            curr += letter
11            # if unique
12            if curr not in theset:
13                ans.append(curr)
14                theset.add(curr)
15                curr = ""
16            # else if not unique, then continue from it until it is
17    
18            
19        return ans