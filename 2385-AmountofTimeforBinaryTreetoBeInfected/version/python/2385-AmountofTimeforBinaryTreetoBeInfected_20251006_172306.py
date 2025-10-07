# Last updated: 10/6/2025, 5:23:06 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # change tree into graph (adj list) so we can go multiple direction
        # parent and child would be its neighbors
        adj = defaultdict(list)
        # all node values are distinct

        # You don’t need to capture the recursive returns at all — just connect directly inside the recursion.
        def dfs(root, parent):
            if not root:
                return
            # pre or post order will both work
            dfs(root.left, root)
            dfs(root.right, root)
            # just think about at that moment that child and that parent. no need worry about this node's children. make that connection between these two nodes and this will populate
            if parent:
                adj[parent.val].append(root.val)
                adj[root.val].append(parent.val)
            return
        dfs(root, None)
        # now we have everything in adj list so we could do a bfs to start from infected node and go level by level until done
        q = deque([start])
        visited = set([start])
        time = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    # need this else infinite loop of appending unless u delete neighbors from hashmap but nah
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            time += 1
        return time - 1 # bc it will increment one extra time after all nodes exhausted