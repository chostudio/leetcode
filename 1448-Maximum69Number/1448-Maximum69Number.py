# Last updated: 9/11/2025, 12:31:07 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        # obv way is to string, and then update the first 6 u see into a 9 from left to right. not sure how to do it where O(1) space
        arr = list(str(num))
        for i in range(len(arr)):
            if arr[i] == "6":
                arr[i]="9"
                break
        return int("".join(arr))