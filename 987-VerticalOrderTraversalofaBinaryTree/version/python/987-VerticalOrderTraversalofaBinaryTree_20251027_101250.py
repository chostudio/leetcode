# Last updated: 10/27/2025, 10:12:50 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # just go through dfs or bfs and sort the final thing at the end who cares time complexity lol

        # bc we dont know how many use hashmap first for storage then ans arr at the end
        position = defaultdict(list)
        # (level, rightleft) as key to list then figure out how to iterate L to R. maybe pre order traversal and visited set? or keep track of smallest to bigggest adn iterate thorugh that range
        # actually kepp max height of tree then when you append into ans it goes from leftmost column bc in 0 column it's 1, 5, 6, but b4 you append arrays together you it need to sort
        leftmost = inf
        rightmost = -inf
        maxheight = 0
        def dfs(root, level, horizontal):
            if not root:
                return
            nonlocal leftmost 
            leftmost = min(leftmost, horizontal)
            nonlocal rightmost 
            rightmost = max(rightmost, horizontal)
            nonlocal maxheight # kind of need to init them first on a separate line
            maxheight = max(maxheight, level)
            position[(level, horizontal)].append(root.val)
            dfs(root.left, level + 1, horizontal - 1)
            dfs(root.right, level + 1, horizontal + 1)

        dfs(root, 0, 0)
        ans =[]
        for i in range(leftmost, rightmost + 1):
            col = []
            for j in range(0, maxheight+1):
                if (j, i) in position:
                    temp = position[(j, i)]
                    temp.sort()
                    for k in temp: # in order to not get an additional triple bracket inside
                        col.append(k)
            ans.append(col)
        return ans
        # a slightly faster way to do it is to append to final answer array as you go and use a horizontal mirroring trick to compare the variables that would be at the same position eg. 5 and 6. since they'll only be 2 at max at the same position just input them in asc order into final answer array one at a time