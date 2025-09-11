# Last updated: 9/11/2025, 12:30:32 PM
class Solution:
    def sortVowels(self, s: str) -> str:
        # loop through string, remember the index and what the voel letter is (two arrays). then sort the vowel letter array. change og stirng to an array ( we so can replace/overwrite individual elements). loop through sorted letter and index arrays at same time (they are sam elength) and overwrite. rejoin string. return.
        indicies = []
        letters = []
        vowels = ["a", "A", "e", "E", "i", "I", "O", "o", "u", "U"]
        for i in range(len(s)):
            if s[i] in vowels:
                indicies.append(i)
                letters.append(s[i])
        letters.sort()
        arr = list(s)
        for i in range(len(letters)):
            arr[indicies[i]] = letters[i]
        return "".join(arr)