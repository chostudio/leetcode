# Last updated: 9/11/2025, 12:31:18 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 == str2 + str1:
            len1, len2= len(str1), len(str2)
            divisor=min(len1, len2)
            while divisor > 0:
                if len1%divisor == 0 and len2%divisor == 0:  
                    break 
                divisor -= 1
            return str2[:divisor]
        else:
            return ""
