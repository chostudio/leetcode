# Last updated: 9/11/2025, 12:30:45 PM
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxVal = 0
        for i in range(len(number)):
            if number[i] == digit:
                maxVal = max(maxVal, int(number[0:i]+number[i+1:]))
        return str(maxVal)
                