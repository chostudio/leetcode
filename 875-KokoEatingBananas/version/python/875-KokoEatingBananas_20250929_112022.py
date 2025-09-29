# Last updated: 9/29/2025, 11:20:22 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_speed(eating_speed):
            count_hours = 0
            for pile in piles:
                count_hours += math.ceil(pile / eating_speed) # need to round up not round down ( which is python default division towards zero) (bc even if pile == 3 and eating_speed = 2, then it would take 1.5 hours which means 2 hours, must round upwards)
            return count_hours <= h

        # binary search the range of speeds not the piles amounts. (len of piles) * log(h) time complexity bc we go through piles every time to check
        low = 1 # cant eat 0
        high = max(piles) # worst case is just eat max every time since we are guarenteed that h (hours) will be a eatable value amount

        smallest = high # can only go lower so set to highest value first
        while low < high:
            mid = (low + high) // 2
            check = valid_speed(mid)
            if check == True:
                smallest = min(smallest, mid)
                # if valid then lets go smaller
                high = mid
            else:
                # not valid at mid so we need to make bigger
                low = mid + 1
        return smallest
