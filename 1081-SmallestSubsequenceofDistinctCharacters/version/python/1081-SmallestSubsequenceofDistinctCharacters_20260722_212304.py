# Last updated: 7/22/2026, 9:23:04 PM
1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        # stack but why in this case
4        freq = Counter(s)
5        smallest = inf
6        isinstack = set()
7        stack = []
8
9        for letter in s:
10            freq[letter] -= 1 # this is a letter, we are seeing it. we may or may not use it. decrementing in th beginning
11            # greediing the shortest smallest substring bc SUBSEQUENCE of removing letters
12            while stack and freq[stack[-1]] > 0 and stack[-1] > letter and letter not in isinstack:
13                # note that we wouldn't want to have currletter pop out things before if we aren't even going to add it e.g. aba "a" would pop out the b in the second go around IF we didn't have the letter not in stack alr
14                # oh i see why monotonic stack. we want to get rid of bigger chars in the stack by popping out them and then putting letter in
15                prevchar = stack.pop() # can we pop that last letter out if 
16                isinstack.remove(prevchar)
17            # ideally, smallest letters first
18            # basically, do we take this letter or not YES if we dont want a duplicate letter in it
19
20            if letter not in isinstack:
21                isinstack.add(letter)
22                stack.append(letter)
23
24        return "".join(stack)