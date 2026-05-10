# Last updated: 5/9/2026, 8:15:58 PM
1class Solution:
2    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
3        hashmap = defaultdict(int)
4        currword = []
5
6        letters = "qwertyuiopasdfghjklzxcvbnm"
7
8        for s in range(len(chunks)):
9            string = chunks[s]
10            # print(string)
11            for letter in range(len(string)):
12                if string[letter] in letters:
13                    currword.append(string[letter])
14                    continue
15                elif string[letter] == "-" and len(currword) > 0 and letter < len(string)-1 and string[letter+1] in letters:
16                    # for i in string
17                
18                    # letter > 0 and letter < len(string)-1 and string[letter-1] in letters and string[letter+1] in letters:
19                    # print(string[letter])
20                    currword.append(string[letter])
21                    continue
22                elif string[letter] == "-"  and len(currword) > 0 and letter == len(string)-1 and s < len(chunks)-1 and chunks[s+1][0] in letters:
23                    currword.append(string[letter])
24                    continue
25                    
26                else: #invalid
27                    if len(currword) > 0:
28                        word = "".join(currword).strip()
29                        hashmap[word] += 1
30                        currword = []
31        if len(currword) > 0:
32            word = "".join(currword)
33            hashmap[word] += 1
34        print(hashmap)
35        ans = []
36        for q in queries:
37            amount = hashmap[q] if q in hashmap else 0
38            ans.append(amount)
39        return ans