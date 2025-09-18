# Last updated: 9/17/2025, 2:14:35 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # number one thin is we quit out when length of n
        # dfs (or stack) is the brute force way O(2^2n) exponential
        ans = []
        # instead of having a stack it makes it easier to just directly pass a empty string in parameters (duplicating it, no need worry about arr to str at the end)
        
        def dfs(open, close, s):
            if open == close and open + close == n * 2:
                ans.append(s)
                return
            if open < n:
                dfs(open + 1, close, s + "(")
                # why pop? other than just bc it's backtracking
            
            if close < open: # less than open
                dfs(open, close + 1,  s + ")")

        dfs(0, 0, "")
        return ans