# Last updated: 9/18/2025, 6:56:52 PM
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        cities = defaultdict(set)
        for t in transactions:
            name, time, money, city = t.split(",")
            cities[(int(time), name)].add(city)
        

        invalid = []
        for t in transactions:
            name, time, money, city = t.split(",")
            if int(money) > 1000:
                invalid.append(t)
                continue
            
            for i in range(int(time)-60, int(time)+61):
                if (i, name) in cities:
                    cities1 = cities[(i, name)]
                    if len(cities1 - {city}) > 0: # it's zero. why zero? if there was only one city and it was the city that we were at, it would have been removed. but since there is still SOMETHING there, then it's invalid bc different city that wasn't removed
                        invalid.append(t)
                        break # forgot a break early
        return invalid