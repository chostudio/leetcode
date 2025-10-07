# Last updated: 10/6/2025, 9:05:53 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        def recurse(num):
            totalsum = 0
            while num > 0:
                number = num % 10
                totalsum += number * number
                num //= 10
            if totalsum == 1:
                return True
            if totalsum in visited:
                return False
            visited.add(totalsum)
            return recurse(totalsum) # YOU FORGOT the return keyword. must have a return keyword since you want to eventually return true or false
        visited.add(n)
        return recurse(n)