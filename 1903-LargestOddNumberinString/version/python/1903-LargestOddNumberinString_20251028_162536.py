# Last updated: 10/28/2025, 4:25:36 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # starting from the rightmost odd number go left and return as far as you can.
        for i in range(len(num)-1, -1, -1):
            # you mix up the index and value watch out. mod needs to be odd
            if int(num[i]) % 2 == 1 and num[i] != "0":
                return num[:i+1] # include i at end. splice is exclusive at end
        return "" # no odd