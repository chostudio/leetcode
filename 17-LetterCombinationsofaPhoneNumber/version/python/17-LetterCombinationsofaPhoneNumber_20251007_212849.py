# Last updated: 10/7/2025, 9:28:49 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # needs to be strings as keys bc the digits is a string
        lettermap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans = []
        def dfs(i, word):
            # could also be "i" instead of len word
            if len(word) == len(digits):
                ans.append(word)
                return
            for letter in lettermap[digits[i]]:
                dfs(i + 1, word + letter)
        
        # set up requires there to be digits else dont acidentally call the function
        if len(digits) > 0:
            dfs(0, "") # needs to be 0, ""
        return ans