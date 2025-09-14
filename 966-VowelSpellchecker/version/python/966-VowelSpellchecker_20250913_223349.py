# Last updated: 9/13/2025, 10:33:49 PM
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # to not get O(n) to check words in wordList, convert into hashmap. additionally we will have a wildcard for any vowels "*" - bc any individual vowel can be replaced and it ll still work
        regular = set(wordlist)
        vowel = collections.defaultdict(str)
        capital = collections.defaultdict(str)

        for word in reversed(wordlist): # we want to return first appearance (if there is two identical words after the thing we want it to return the first one so we go backwards and the last overwrite will be the first)
            arr = list(word.lower())
            for letter in range(len(arr)):
                if arr[letter] in "aeiou":
                    arr[letter] = "*"
            newWord = "".join(arr) # new word acts as key
            vowel[newWord] = word
            capital[word.lower()] = word
        
        ans = []
        for word in queries:
            if word in regular:
                ans.append(word)
                continue
            if word.lower() in capital:
                ans.append(capital[word.lower()])
                continue
            arr = list(word.lower())
            for letter in range(len(arr)):
                if arr[letter] in "aeiou":
                    arr[letter] = "*"
            newWord = "".join(arr) # new word acts as key
            if newWord in vowel:
                ans.append(vowel[newWord])
                continue
            ans.append("")
        return ans

