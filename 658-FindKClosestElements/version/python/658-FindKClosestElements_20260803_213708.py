# Last updated: 8/3/2026, 9:37:08 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        # lowk i would binary search log n to find the number.
4        # then i would (assumign its in the arra) go left and go right and then check which oen slocser. if edge then always take the other one duh. actually worst case is still O(n) so it doesnt matter anyway just init from start and break when no longer getting better
5        # if at ends then edge case.
6        # if number not in array ( can check O(1) time then just return start or end. or just sliging dinwo from start with deque of indicies. check left most and right most compare when thinking about adding a new one
7
8        ans = deque()
9        for num in arr:
10            if len(ans) < k:
11                ans.append(num)
12                continue
13            # okay now we have k values so lets compare and pop if necessary
14            a= ans[0]
15            b = num
16            if abs(b - x) < abs(a - x):
17                # pop and shift
18                ans.popleft()
19                ans.append(num)
20                continue
21            # if they're equal then we dont do anything
22            # elif abs(b - x) == abs(a - x):
23            #     continue
24            # if ab(b -x) is greater than smallest, then we can break at this point bc we know everything will just be further honestly
25            if abs(b - x) > abs(a - x):
26                break
27        return list(ans)