# Last updated: 8/3/2026, 8:24:14 PM
1class Solution:
2    def removeDuplicateLetters(self, s: str) -> str:
3        # we first go through and get the freq of every letter.
4        freq = Counter(s)
5        # the reason for this is obv we could pop out a letter if its in the stack and bigger than our current letter, but we do not pop the letter out if there's no more of it later as in is this the last letter of its kind and as we iterate through the thing we decrement
6        # so this is monotonic stack but with a caveat -- this can probably be applied in other similar scenarios too.
7        # bc smallest in lexographical order. cannot move around letters otherwise make it way easier
8        stk = []
9        ss = set()
10        for char in s:
11            # we need char not in ss bc it doesnt make sense for a char to just ruin everyone else if its already in the current set you know
12            while stk and stk[-1] > char and freq[stk[-1]] >= 1 and char not in ss: # has to be at least 1 or more bc if there's one more after the current letter then that means its totally okey dokey to pop the one in the stack out bc theres at least one more
13                oldchar = stk.pop()
14                ss.remove(oldchar)
15            # only add the character if its nort already inside the end result otherwise we dont want to double add it duh
16            if char not in ss:
17                stk.append(char)
18                ss.add(char)
19            freq[char]-= 1 # 
20            
21
22        return "".join(stk)