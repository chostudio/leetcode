# Last updated: 7/27/2026, 8:09:42 PM
1class Trie:
2    # dont forget self in the parem function
3    def __init__(self):
4        self.letters = {}
5        self.word = ""
6    
7    # rememebr to add self to every beginign parameter
8    def addword(self, word):
9        node = self # can i do this? refer to the node thats calling the function?
10        # prev = self
11        for letter in word:
12            if letter not in node.letters:
13                # then we got to make a new node for it
14                node.letters[letter] = Trie()
15            # prev = node
16            node = node.letters[letter] # move curr to the next
17            
18        # now we are at the last letter node of the word
19        node.word = word # assign the word to the last so we know it's a word. there's like a weird off by one kinda thing going on there the last node/letter should contain the full word. but how this for loop is like is we go +1 past the last letter and so it's kinda weird so i did this prev trick, probably better way to do it
20
21class Solution:
22    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
23        
24
25
26        # its backtracking becauase we remove the letter from the visited set before we go back to the prev letter. i think that makes sense. if we reset visited set one time outside, it would not work bc one we visit letter we cant visit letter again, which is not true bc you have to go to the same box from another letter path possibly
27        
28        def dfs(r, c, node, visited):
29             # else this letter matches this node letter
30
31            if node.word != "":
32                nonlocal ans
33                ans.add(node.word)
34
35            if r < 0 or r >= n or c < 0 or c >= m:
36                return
37            if (r, c) in visited:
38                return
39            if board[r][c] not in node.letters:
40                return
41           
42
43            # else, continue down the path (one word could be subset of another word)
44            visited.add((r, c))
45            nextnode = node.letters[board[r][c]]
46            # go in all directions
47            dfs(r+1, c, nextnode, visited)
48            dfs(r-1, c, nextnode, visited)
49            dfs(r, c+1, nextnode, visited)
50            dfs(r, c-1, nextnode, visited)
51
52            visited.remove((r, c))
53        
54        # do the trie stuff first
55        start = Trie()
56        for word in words:
57            start.addword(word)
58
59        n, m = len(board), len(board[0])
60        ans = set()
61        # starting from each point on the grid
62        for r in range(n):
63            for c in range(m):
64                visited = set()
65                dfs(r, c, start, visited)
66        
67        return list(ans)