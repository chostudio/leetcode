# Last updated: 9/11/2025, 12:31:13 PM
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # two loops
        times = defaultdict(set)
        for t in transactions:
            name, time, amount, city = t.split(",")
            time = int(time)
            times[(time, name)].add(city)
        
        invalid = [] #has to be list bc if two identical u have to count both
        for t in transactions:
            name, time, amount, city = t.split(",")
            time = int(time)
            amount = int(amount) # reminder that you need to int the amount
            if amount > 1000:
                invalid.append(t)
                continue
            for i in range(time-60, time+61):
                if (i, name) in times:
                    cities = times[(i, name)]
                    # you HAVE to do it this way. bc no dups unless same set
                    if len(cities - set([city])) >= 1: 
                        invalid.append(t)
                        break
        return invalid