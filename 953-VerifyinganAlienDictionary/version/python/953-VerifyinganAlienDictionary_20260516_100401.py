# Last updated: 5/16/2026, 10:04:01 AM
1class Solution:
2    def isAlienSorted(self, words: List[str], order: str) -> bool:
3        if len(words) <= 1:
4            return True
5        
6        # at least two for two pointer approach
7        # prolly use the linkedlist else trick, set "nothing" as -1/earlier, it's a value smaller than any letter when comparison
8
9        hashmap = defaultdict(int)
10        for l in range(len(order)):
11            hashmap[order[l]] = l
12        for i in range(len(words)-1):
13            # remember to actually move the words using i as index, i + 1
14            firstword = words[i]
15            secondword = words[i+1]
16
17            for l in range(max(len(firstword), len(secondword))):
18                letter1 = hashmap[firstword[l]] if l < len(firstword) else -1
19                letter2 = hashmap[secondword[l]] if l < len(secondword) else -1
20
21                if letter1 < letter2: # all is right and move onto next two words
22                    break # from this inner for loop for letters
23                # otherwise we keep on going if the letters are the same
24                elif letter1 == letter2:
25                    continue
26                # you cant JUST ONLY do the below, without the above, bc it doesnt consider the other possiblities
27                else: # if letter2 < letter1:
28                    return False
29
30        return True