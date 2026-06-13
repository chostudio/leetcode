# Last updated: 6/12/2026, 10:47:08 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        adj = defaultdict(list)
4
5        for a, b in prerequisites:
6            # a requires taking b first
7            adj[a].append(b)
8        
9        
10        def dfs(course):
11            if course in path:
12                return False
13            #if course not in path but in visited
14            if course in visited:
15                return True # already checked it
16            
17            # thus the course is not in our path or visited, default unchecked state
18
19            path.add(course) # we add the course to the path (current cycle)
20            for prereq in adj[course]:
21                if dfs(prereq) == False:
22                    return False
23            
24            # otherwise we get through all the prereqs safely
25            path.remove(course)
26            ans.append(course)
27            visited.add(course) # out of current cycle, verify it forever for other cycles
28            return True
29
30        ans = []
31        path = set()
32        visited = set()
33        for i in range(numCourses):
34            if dfs(i) == False:
35                return []
36            # else true, keep on going, reset path every iteration
37            path = set()
38
39        return ans