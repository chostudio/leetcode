# Last updated: 9/11/2025, 12:31:16 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in address:
            if i == ".":
                ans += "[.]"
            else:
                ans += i
        return ans