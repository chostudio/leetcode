# Last updated: 10/16/2026, 11:27:29 PM
1class Solution:
2    def breakPalindrome(self, palindrome: str) -> str:
3        # replace the very first non 'a'. if the mirror equivalent in the string is NOT 'a' as well otherwise impossible. becuase we wantthe smallest lexigraphically, we cannot change a to a b for example
4
5        for i in range(len(palindrome) // 2): # must stop halfway
6            if palindrome[i] != "a" and palindrome[len(palindrome) - i - 1] != "a":
7                return palindrome[:i] + "a" + palindrome[i+1:]
8            # apparently in this question aa should be ab
9            # so if we past the halfway point, 
10
11        # in the case where it's all As we need to flip the last a into a b, what an edge case
12        if len(palindrome) > 1: # e.g. not just a simgle letter
13            return palindrome[:len(palindrome)-1] + "b" 
14        return "" # impossible