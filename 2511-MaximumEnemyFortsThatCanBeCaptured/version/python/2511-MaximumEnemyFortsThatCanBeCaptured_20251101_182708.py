# Last updated: 11/1/2025, 6:27:08 PM
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # if max(forts) == 0 or min(forts) == 0:
        #     return 0
        # 2 pass lr, rl insteaod of on^2
        maxarmy = 0
        length = 0
        haveseenone = False
        for i in range(len(forts)):
            if forts[i] == 1:
                length = 0
                haveseenone = True
            elif forts[i] == -1:
                maxarmy = max(maxarmy, length)
                length = 0
                haveseenone = False # must reset
            elif forts[i] == 0 and haveseenone:
                length += 1
        
        # make sure to reset length
        length = 0
        haveseenone = False
        for i in range(len(forts)-1, -1, -1):
            if forts[i] == 1:
                length = 0
                haveseenone = True
            elif forts[i] == -1:
                maxarmy = max(maxarmy, length)
                length = 0
                haveseenone = False # must reset
            elif forts[i] == 0 and haveseenone:
                length += 1

        return maxarmy