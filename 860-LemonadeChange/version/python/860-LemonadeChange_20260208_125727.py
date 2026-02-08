# Last updated: 2/8/2026, 12:57:27 PM
1class Solution:
2    def lemonadeChange(self, bills: List[int]) -> bool:
3        # collect from least to greatest, so get all the fives first, then all the tens, then all the twenties. We can technically do this in all of one space complexity O(n) time. 
4
5# Instead of using a hash map because we only know we have three possible bills, we can just have three variables of how much of each five, ten, and twenty dollar bills we have. 
6        fives = 0
7        tens = 0
8        # you cannot sort it, customers are in a queue, so you have to go left or right, one pass. 
9        for bill in bills:
10            if bill == 10:
11                if fives == 0:
12                    return False
13                fives -= 1
14                tens += 1
15            if bill == 20:
16                if tens >= 1 and fives >= 1:
17                    tens -= 1
18                    fives -=1 
19                    # we actually dont care about 20s unless we adding them all up at the end which we arent in this case
20                elif fives >= 3:
21                    fives -= 3
22                else:
23                    return False
24            if bill == 5:
25                fives += 1
26        return True