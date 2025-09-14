# Last updated: 9/13/2025, 9:55:58 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        # dont overthink it. look at the four steps it lists it in order of what to do

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        negative = 1
        if i < len(s) and s[i] == "-":
            negative = -1 # make sure it's a number (if u do that route) + single equal sign not double (typo)
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        
        # now it's a number. possibly 0
        num = 0
        while i < len(s) and s[i].isdigit(): # check length first so not out of bounds
            num = num * 10 + int(s[i])
            i += 1 # make sure not infinite
        
        num *= negative
        if num > 2**31 -1:
            num = 2**31 -1
        elif num < -2**31:
            num = -2**31 # dont forget equal sign here too
        return num