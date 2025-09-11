# Last updated: 9/11/2025, 12:32:04 PM
from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # took a second but i think this is an easy if i get this right
        secretString = str(secret)
        guessString = str(guess)
        cows = 0
        bulls = 0
        hashmap = defaultdict(list)
        for i in range(len(secretString)):
            # one number can be in multiple indexes which is why list instead of just int
            hashmap[secretString[i]].append(i)
        print(hashmap)
        amount = defaultdict(int)
        for i in range(len(secretString)):
            amount[secretString[i]] = len(hashmap[secretString[i]])

        # first go through guess string and only count the numbe rof 1:1 matches for cows
        for x in range(len(guessString)):
            if guessString[x] in hashmap.keys():
                if x in hashmap[guessString[x]]:
                    bulls += 1
                    amount[guessString[x]] -= 1
        
        # then cows separately after
        for x in range(len(guessString)):
            if guessString[x] in hashmap.keys():
                # checking if index matches
                if x not in hashmap[guessString[x]]:
                    if amount[guessString[x]] > 0:
                        cows += 1
                    amount[guessString[x]] -= 1

                # del hashmap[secretString[x]] # remove to not double cout it
        return "" + str(bulls) + "A" + str(cows) + "B"