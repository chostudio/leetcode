# Last updated: 9/11/2025, 12:31:09 PM
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # misread question. theree will alwasy be two integers. just need to find combo that niehter have a 0 in them
        arr = [1, 1]
        for i in range(n):
            # the easiest way is to just use a string based check to make sure there is no 0s in the number. you could to palindrom check for zeros for better space complaexity but strings make it faster to see if there's a zero at all
            if "0" not in str(i) and "0" not in str(n-i):
                arr[0] = i
                arr[1] = n - i
                return arr