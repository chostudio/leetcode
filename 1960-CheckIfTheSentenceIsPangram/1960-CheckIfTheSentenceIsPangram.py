# Last updated: 9/11/2025, 12:30:51 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        alphabet = set(alphabet)
        for i in sentence:
            if i.isalnum() and i in alphabet:
                alphabet.remove(i.lower())
        return len(alphabet) == 0