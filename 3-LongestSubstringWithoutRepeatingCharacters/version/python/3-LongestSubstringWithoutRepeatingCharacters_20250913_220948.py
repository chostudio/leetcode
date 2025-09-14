# Last updated: 9/13/2025, 10:09:48 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap, store letter index. remember that this is a sliding window question so must have two vars.
        hashmap = collections.defaultdict(int)
        longest = 0 # bc possible that string is 0 length
        left = 0 # left is liket he left boundry of our imaginary sliding window
        for i in range(len(s)):
            # if letter in hashmap. cannot have duplicates
            if s[i] in hashmap and left <= hashmap[s[i]]: # don't go backwards if not needed. MUST have <= because we want this condition to trigger to move the left index + 1 to not include the duplicate
                left = hashmap[s[i]] + 1 # yues you need plus one so we dont include the character
                 # move all the way up to most curr index
            else: # not in hashmap, so we dont need to reupdate and there's a chance this could be the longest
                longest = max(longest, i - left + 1)
            hashmap[s[i]] = i # hilariously, we do this for both either way bc we need to keep track of what char we;ve seen always. make sure to not forget this
        return longest

