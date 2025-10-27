# Last updated: 10/27/2025, 10:23:07 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # okay so this is bfs but you switch the direction on the level every other level first go pos then go neg
        # order in which you put the child into the q also matters. maybe r then left depending on the thing
        # absolute easiest but worst time is just normal bfs and reverse before appending every other level
        if not root: # base case if nothing there
            return []
        ans = []
        q = deque([root])
        backwards = False
        while q:
            temp = []
            level = len(q)
            for _ in range(level):
                node = q.popleft()
                temp.append(node.val) # values not the actual node itself
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if backwards:
                temp.reverse() # in place
            backwards = not backwards # flip boolean
            ans.append(temp)
        return ans