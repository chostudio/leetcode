# Last updated: 11/1/2025, 3:06:07 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycl detection checking. adj list. technically doesn matter which way u set up adj list bc if there is cycle it will be there no matter what
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        

        def dfs(course, visitstatus):
            if visitstatus[course] == 1: # we're curr visitng it but visitng it again which therefore menas cycle
                return False
            if visitstatus[course] == 2: # already visited in prev check and determined it's good
                return True
            
            # else havent visited yet so change to visitng currently
            visitstatus[course] = 1

            # cannot bleive the same logic if in here as in the main func
            for prereq in adj[course]:
                if dfs(prereq, visitstatus) == False:
                    return False

            visitstatus[course] = 2 # at very end now we can mark as sucessful visit 
            return True


        # 0 is not yet visited, 1 is visiting, 2 is alr visited and good
        visitstatus = [0] * numCourses
        for course in range(numCourses):
            if dfs(course, visitstatus) == False:
                return False
        return True # else we go through all and nothing triggers then return true