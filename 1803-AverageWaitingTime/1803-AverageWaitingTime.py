# Last updated: 9/11/2025, 12:30:56 PM
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sum = 0
        curr = 0
        for i in range(len(customers)):
            arrive, finish = customers[i]#[0], customers[i][1]
            if arrive > curr: # if arrive and can immideate start
                curr = arrive + finish
            else:
                curr += finish # just add the time their meal takes to make
            sum += curr - arrive
        return float(sum / len(customers))
