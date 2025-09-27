# Last updated: 9/27/2025, 12:30:05 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recurse num of left then num of right when both equal each aother and max amiutr then return
        ans = []
        def backtrack(open, close, parens):
            if open == close == n:
                ans.append(parens)
                return
            if open <n:
                backtrack(open + 1, close, parens + "(")
            if close < open: #close is based on open, have to be after open, else wouldnt match up
                backtrack(open, close + 1, parens + ")")
        backtrack(0, 0, "")
        return ans