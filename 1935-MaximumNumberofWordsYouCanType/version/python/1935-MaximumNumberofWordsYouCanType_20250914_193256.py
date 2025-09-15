# Last updated: 9/14/2025, 7:32:56 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        unusable = set(list(brokenLetters))
        # no leading or trailing spaces
        # single pointer loop instead of splitting text into array
        amount = 0
        i = 0
        while i < len(text):
            if text[i] in unusable:
                while i < len(text) and text[i] != " ":
                    i += 1
            elif text[i] == " " or i + 1 == len(text):
                print(text[i])
                amount += 1
            i += 1
        return amount
        # if you want to control the index integer var in a loop, you have to use a while loop. even if you try edit the number in a for loop, it'll always increment by one/however much and go to the next predetermined val after