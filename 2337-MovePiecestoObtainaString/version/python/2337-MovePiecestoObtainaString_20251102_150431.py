# Last updated: 11/2/2025, 3:04:31 PM
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False # if not exactly the same stirng without the lines
        
        # weve guarenteed that order is correct, now we must check index as in if L and R can actually be moved in the correct direction only. e.g. if a target L is too far right then we cannot move it therefore false
        s, t = 0, 0
        n = len(start)
        while s < n and t < n:
            # move the pointers up to the next actual letter for them
            # make sure in bounds first
            while s < n and start[s] == "_":
                s += 1
            while t < n and target[t] == "_":
                t += 1
            if s == n or t == n: # done bc we've gone past letters
                break
            
            # now they msut be at a letter, guarenteed that same letter but must check index
            if start[s] == "L":
                if t > s: # target is to the right of start, impossible
                    return False
            elif start[s] == "R":
                if s > t: # target is to the left of the R, impossible
                    return False
            s +=1 
            t += 1 # you need to remember to increment both of them by one at the end otherwise wont ever move up
        return True