# Last updated: 9/11/2025, 12:31:43 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1arr = [0] * 26
        s2arr = [0] * 26
        matching = 0
        if len(s1) > len(s2):
            return False # not possible
        for i in range(len(s1)):
            # HAVE TO ord the letter first so it's number - number and not a char still
            s1arr[ord(s1[i])-ord('a')] += 1
            s2arr[ord(s2[i])-ord('a')] += 1

        # check to see how much matching inisitially. 26!!! not len(s1)
        for i in range(26):
            # make sure to check arr here, not s1, s2. maybe better naming
            if s1arr[i] == s2arr[i]:
                matching += 1
        if matching == 26: return True # if all char freqs match off the bat
        for i in range(len(s1), len(s2)):
            # add, update matching
            s2arr[ord(s2[i])-ord('a')] += 1
            # now is matching
            if s2arr[ord(s2[i])-ord('a')] == s1arr[ord(s2[i])-ord('a')]:
                matching += 1
            # was matching now isn't
            elif s2arr[ord(s2[i])-ord('a')]-1 == s1arr[ord(s2[i])-ord('a')]:
                matching -= 1

            # remove, update matching
            s2arr[ord(s2[i-len(s1)])-ord('a')] -= 1
            # now is matching
            if s2arr[ord(s2[i-len(s1)])-ord('a')] == s1arr[ord(s2[i-len(s1)])-ord('a')]:
                matching += 1
            # was matching now isn't
            elif s2arr[ord(s2[i-len(s1)])-ord('a')]+1 == s1arr[ord(s2[i-len(s1)])-ord('a')]:
                matching -= 1

            # check matching
            if matching == 26: return True
        return False