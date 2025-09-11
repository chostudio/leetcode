# Last updated: 9/11/2025, 12:30:23 PM
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # remember to check logic. hash the reverse as that is what you reference and use og substring to check
        myset = set()
        
        reverse = s[::-1]
        for i in range(len(s)-1):
            myset.add(reverse[i]+reverse[i+1])
            
        for i in range(len(s)-1):
            if (s[i] + s[i+1]) in myset:
                return True
        return False