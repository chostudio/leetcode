# Last updated: 10/29/2025, 11:03:14 AM
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # intervals when not obvious. bc you cannot go inbetween a rect and you also want to split on the rect so just always check on the lines and make sure you can do at least two in either direction
        xintervals = []
        yintervals = []
        for xs, ys, xe, ye in rectangles:
            xintervals.append([xs,xe])
            yintervals.append([ys,ye])
        
        xintervals.sort()
        yintervals.sort()
        def overlap(intervals):
            # tech dont need to merge intervals, why? what if overlap
            stack = []
            for start, end in intervals:
                if len(stack) != 0 and stack[-1][1] > start:
                    stack[-1][1] = max(stack[-1][1], end)
                else:
                    stack.append([start, end])
            
            # then count and iterate through all the start AND end values. but keep track of which ones you're going with and with a set and then return true or false
            # dont need to use a set you can just use a max end var. you iterate from start to end and only check start and prev end


            count = 0
            prev_end = stack[0][1]
            # firsr interval doesnt bc that's its prev end so dw
            for start, end in stack:
                if start >= prev_end:
                    count += 1 # but at the same time we dont want dups -- well we wouldn't get dups bc we don't count prev end and we merged all the intervals earlier anyways
                prev_end = max(prev_end, end) # ONLY CHANGE PREV END TO SEE WHCIH HAS THE GRATEST END VALUE DUHHHHHHHHH NOT START
            return count >= 2

        return overlap(xintervals) or overlap(yintervals)