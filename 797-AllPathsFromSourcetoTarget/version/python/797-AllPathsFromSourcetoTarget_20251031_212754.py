# Last updated: 10/31/2025, 9:27:54 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # maybe dont need to make adj list since input is good alr? just bfs through it and keep track of path if reach end then add onto ans arr?
        ans = []
        
        # cant really do a visited ish set bc its like multipl can be counted. maybe a for loop for all the things? technically there'll be no duplicates bc they all point to diff things?
        # ((0, 0)) # int obj is not subscriptable means there are literally just two zeros in this tuple, not one tuple un a tuple apparently?
        q = deque([(0, [0])]) # node we going to and the path
        while q:
            # node is to be added, has not been added to path yet
            tup = q.popleft()
            print(tup)
            node = tup[0]
            path = tup[1]
            for child in graph[node]:
                newpath = path.copy()
                newpath.append(child) # so we dont have to worry abotu deep copy and editing the path
                # if end vs not
                if child == len(graph) - 1: # end
                    ans.append(newpath)
                else:
                    q.append((child, newpath))
                
        return ans