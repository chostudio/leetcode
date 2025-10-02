# Last updated: 10/1/2025, 7:31:22 PM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x, n):
            # we are only changing n so it makes sense to only care about n in the conditional and we need to return x sometime otherwise 1*1*1 will be 1 if there was only it
            if n == 0:
                return 1
            if n == 1:
                return x
            
            value = recurse(x, n//2)
            new = value * value
            if n % 2 == 1: #if odd, then one more
                return new * x # NOT another value bc we dont know how much is that but we know how much x (our base value) is
            else:
                return new
        
        value = recurse(x, abs(n))
        if n < 0:
            return 1 / value
        return value
        
            