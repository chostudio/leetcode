# Last updated: 9/11/2025, 12:30:25 PM
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        #first add up all the apple amount in the apple arr
        appleCount = sum(apple)
        
        #sort the array (in descending order hence the reverse)
        capacity.sort(reverse = True)

        # i acts as the iterative variable and the number of boxes
        i = 0
        while appleCount > 0:
            # minus the value of the box compared to the apples
            appleCount -= capacity[i]
            i += 1
        return i