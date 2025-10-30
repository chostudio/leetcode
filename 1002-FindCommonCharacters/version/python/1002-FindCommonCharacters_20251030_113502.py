# Last updated: 10/30/2025, 11:35:02 AM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        thefreq = Counter(words[0])
        # hashMAP bc duplicates are allowed

        for word in words:
            wordmap = Counter(word)
            newmap = defaultdict(int)
            for char in thefreq:
                if char in wordmap:
                    newmap[char] = min(thefreq[char], wordmap[char])
            thefreq = newmap
        ans = []
        for char, amount in thefreq.items():
            for i in range(amount):
                ans.append(char)
        return ans