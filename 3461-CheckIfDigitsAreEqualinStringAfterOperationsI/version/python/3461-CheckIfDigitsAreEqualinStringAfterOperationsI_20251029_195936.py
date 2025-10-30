# Last updated: 10/29/2025, 7:59:36 PM
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # midread question it's actually pascal triangle

        arr = list(s)
        n = len(arr)
        for i in range(n):
            arr[i] = int(arr[i])

        while len(arr)> 2:
            print(arr)

            temp = []

            for i in range(len(arr)-1): # only -1 not -2
                temp.append((arr[i] + arr[i+1]) % 10)
            arr = temp
        return arr[1] == arr[0]