# Last updated: 10/7/2025, 8:48:27 PM
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        # "a"": 2
        # enumerate gives you INDEX (and key) NOT key value
        arr = [(f, letter) for letter, f in freq.items()]
        arr.sort(reverse=True)
        q = deque()
        for f, letter in arr:
            q.append(letter * f)
        return "".join(q)