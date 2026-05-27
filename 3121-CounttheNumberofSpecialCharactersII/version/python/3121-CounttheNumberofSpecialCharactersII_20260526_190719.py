# Last updated: 5/26/2026, 7:07:19 PM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3
4        count = 0
5
6
7        # actually, we need a two pass and furthest right and left of the lowercase and uppercase letter bc we won't know if it's not if it's a one pass. 
8        hashmap = defaultdict()
9        for i in range(len(word)):
10            letter = word[i]
11            if letter.isupper():
12                val = hashmap[letter] if letter in hashmap else inf
13                hashmap[letter] = min(val, i)
14            else: # lowercase
15                val = hashmap[letter] if letter in hashmap else -inf
16                hashmap[letter] = max(val, i)
17        
18
19        for letter, i in hashmap.items():
20            # only trigger for lowercase OR uppercase letter, not both uppercase too otherwise double count
21            # the leftmost uppercase has to be after the right most lowercase
22            if letter.isupper():
23                # you have to remember to hceck that there' ssomething in the hashmaps
24                if letter.lower() in hashmap and hashmap[letter.lower()] < i:
25                    count += 1
26
27        return count