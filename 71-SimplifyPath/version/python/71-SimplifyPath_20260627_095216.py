# Last updated: 6/27/2026, 9:52:16 AM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        # first, split based on the //, this gets rid of the multiple ones
4
5        # the thing you have to worry about is not the names of stuff but rather the '.' and the '..'. eveyrthing else is treat as path name when you rejoin it. if "" nothing then that means it mustve been a doubel slash/end slash so just ignore it
6
7
8        path = path.split("/")
9
10        arr = []
11
12        # part / path is kinda confusing naming
13        for part in path:
14            if part == "" or part == ".": # i think single . means curr working directory so we dont care
15                continue
16            elif part == "..":
17                if len(arr) != 0:
18                    arr.pop() # we actualy remove the last thing in the stack bc we go back up one. but cannot pop if nothing in
19            else:
20                arr.append(part)
21        ans = "/" + "/".join(arr)
22        print(ans)
23        return ans
24
25