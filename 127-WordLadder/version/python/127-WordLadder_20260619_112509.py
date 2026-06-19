# Last updated: 6/19/2026, 11:25:09 AM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3
4        # edgecase where if endword is not in the list of words then its impossible
5        if endWord not in wordList: return 0
6        
7        # bfs using special asterisk
8        adj = defaultdict(list)
9
10        # set up the asterisk
11        for word in wordList:
12            for i in range(len(word)):
13                newword = word[:i] + "*" + word[i+1:]
14                adj[newword].append(word)
15        
16        if beginWord == endWord: return 0 # if case where exactly the same then just return 0
17
18        visited = set()
19        q = deque()
20        q.append(beginWord)
21        count = 1 # has to be init to 1 bc the starting word counts as one. 
22
23        while q:
24            level = len(q)
25            for _ in range(level):
26                word = q.popleft()
27                for i in range(len(word)):
28                    newword = word[:i] + "*" + word[i+1:]
29                    for nei in adj[newword]:
30                        if nei == endWord:
31                            return count + 1
32                        if nei not in visited:
33                            q.append(nei)
34                            visited.add(nei)
35            count += 1
36                #
37        return 0 # else go through all and nothing