# Last updated: 10/9/2025, 1:36:36 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited: # we are currently visitng it in this dfs and therefore cycle if try visit again
                return False
            if adj[course] is None:
                return True
            
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            adj[course]= [] # completely remove for first testcase dont need to check twice
            visited.remove(course)
            return True # must return true at very end if we get here sto verify

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True # ifgettrhough everything