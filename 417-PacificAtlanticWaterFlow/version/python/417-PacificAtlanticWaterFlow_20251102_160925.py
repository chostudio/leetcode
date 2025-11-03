# Last updated: 11/2/2025, 4:09:25 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bascially either dfs from each point or dfs from 1 pacific ocean able 2 atlantic oeacn able and then 3 grab the points that are in both sets for answer maybe set intersection. Or one set and if it's already in there by the time we do the other side then add it into the answer. and then remove it as well
        pacific = set()
        atlantic = set()

        def dfs(r, c, lastval, letter):
            if r >= 0 and r < len(heights) and c >= 0 and c < len(heights[0]):
                currval = heights[r][c]
                if currval >= lastval: # must check if reachable. it also can be the same height and it's fine
                    if letter == "P":
                        if (r, c) in pacific:
                            return
                        else:
                            pacific.add((r, c))
                    elif letter == "A":
                        if (r, c) in atlantic:
                            return
                        else:
                            atlantic.add((r, c))
                    dfs(r + 1, c, currval, letter)
                    dfs(r - 1, c, currval, letter)
                    dfs(r, c + 1, currval, letter)
                    dfs(r, c - 1, currval, letter)
            return
        
        for r in range(len(heights)):
            if (r, 0) not in pacific:
                dfs(r, 0, -1, "P")
        for r in range(len(heights)):
            end = len(heights[0]) - 1
            if (r, end) not in atlantic:
                dfs(r, end, -1, "A")
        
        for c in range(len(heights[0])):
            if (0, c) not in pacific:
                dfs(0, c, -1, "P")
        
        for c in range(len(heights[0])):
            bottom = len(heights) - 1
            if (bottom, c) not in atlantic:
                dfs(bottom, c, -1, "A")
        
        ans = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])
        return ans