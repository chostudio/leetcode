# Last updated: 9/27/2026, 8:24:34 PM
1class Solution:
2    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
3        
4        pair = defaultdict(str)
5        for key, value in knowledge:
6            pair[key] = value
7        
8        arr  = []
9        for char in s:
10            arr.append(char)
11        print(arr)
12
13        i = 0
14        while i < len(arr):
15            if arr[i] == "(":
16                temparr = []
17                arr[i] = "" # remove the letter
18                i += 1
19                while arr[i] != ")":
20                    temparr.append(arr[i])
21                    arr[i] = ""
22                    i += 1
23                
24                word = "".join(temparr)
25                replaceword = "?"
26                if word in pair:
27                    replaceword = pair[word]
28
29                arr[i] = replaceword
30
31            i += 1
32        
33        return "".join(arr)