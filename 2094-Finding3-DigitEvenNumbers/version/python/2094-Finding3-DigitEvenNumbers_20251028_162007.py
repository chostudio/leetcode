# Last updated: 10/28/2025, 4:20:07 PM
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # so on^3 solution is triple for loop, append to array, sort array. is there a faster way to generate permutations of array?
        # a slightly faster way is to count the freq of each digit ussing hashmap then iterate all even numbers from 100-999 to see if it it possible to make this number using the digits and if it is then we append to ans array
        # the same digit can be used as many times as in the array e.g. 2,2,2 can make 222 but only 2,1,2 can only make 22
        freq = Counter(digits)
        ans = []
        for i in range(100, 999, 2):
            # everything is even already possibly
            val = i
            digit1 = val % 10
            val //= 10
            digit2 = val % 10
            val //= 10
            digit3  = val % 10
            val //= 10

            flag = True

            freq[digit1] -= 1
            if freq[digit1] < 0:
                flag = False
            freq[digit2] -= 1
            if freq[digit2] < 0:
                flag = False
            freq[digit3] -= 1
            if freq[digit3] < 0:
                flag = False
            # reset hashmap changes
            freq[digit1] += 1
            freq[digit2] += 1
            freq[digit3] += 1
            if not flag: # if flag is false
                continue

            ans.append(i)
        return ans