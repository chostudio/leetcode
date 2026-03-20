# Last updated: 3/19/2026, 9:36:03 PM
1class Solution:
2    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
3        arr = sentence.split()
4        hashset = set()
5        for word in dictionary:
6            hashset.add(word)
7        
8        for i in range(len(arr)):
9            # python really bad bc having to reconstruct string
10            word = arr[i] 
11            for j in range(len(arr[i])):
12                newword = word[:j]
13                if newword in hashset:
14                    arr[i] = newword
15                    break
16        return " ".join(arr)