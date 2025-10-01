# Last updated: 9/30/2025, 10:10:22 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for char in word:
                # a = 42, b = 43

                temp[ord(char)-ord("a")] += 1
            anagrams[tuple(temp)].append(word)
        print(anagrams.values())
        return list(anagrams.values()) # .values is a set so u need to convert it