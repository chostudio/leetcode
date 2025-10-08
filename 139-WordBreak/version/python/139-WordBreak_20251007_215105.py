# Last updated: 10/7/2025, 9:51:05 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s) # 0 is true
        for i in range(len(s)+1): # +1 bc dp array is +1
            for word in wordDict:
                if i - len(word) >= 0: # index exists
                    if dp[i - len(word)] == True and s[i - len(word):i] == word:
                        dp[i] = True # dont ==, only one = assignment not comparison
                        break # BREAKKKKK REMEMBER TO BREAKKKKKK AFTER
        return dp[-1]