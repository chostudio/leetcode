# Last updated: 10/1/2025, 6:53:00 PM
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = 0
        differences = []
        # send everyone to A first
        for person in costs:
            cost += person[0]
            # to be refunded in the future if necessary
            differences.append(person[1] - person[0])
        
        differences.sort() # least to greatest
        # DO NOT +1 exclusive leave it as //2 why ius that
        for i in range(len(differences) // 2 ): # only halfway, gaurenteed even
            cost += differences[i] # can be negative bc we are refunding too
        return cost