# Last updated: 10/1/2025, 5:24:17 PM
class Solution:
    def checkValidString(self, s: str) -> bool:
        opens, closes = 0, 0
        for char in s:
            if char == "(":
                opens += 1
                closes += 1
            elif char == ")":
                opens -= 1
                closes -= 1
            elif char == "*":
                opens += 1
                closes -= 1
            # its okay if our "all closes" closes less than 0
            if closes < 0:
                closes = 0
            # its not okay if our ideal solution is less than 0
            if opens < 0:
                return False
        return closes == 0 # else we survive return whether opens is 0 equal true because to be valid it needs to be perfect match, which means closes is 0, doesnt matter what opens is bc the accpetable range is [closes, 0, opens] and we limit closes at 0 if under 0 so if 0 then good