# Last updated: 9/28/2025, 4:43:40 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        # idk how to solve o(1) space but should know. ik how to O(n) space tho
        arr = s.split() # dont need to split BY " ", it'll do it automatically for you based on spaces + default way also removes the trailing spaces
        l, r = 0, len(arr) -1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return " ".join(arr)
