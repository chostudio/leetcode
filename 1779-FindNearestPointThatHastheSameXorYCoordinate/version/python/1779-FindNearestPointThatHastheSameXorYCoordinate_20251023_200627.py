# Last updated: 10/23/2025, 8:06:27 PM
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        Mdist = inf
        point = inf
        # how to determine smaller index e.g. 3,4 vs 4,3 ITLL be on the same line so dont worry bc one number will be the seame just compare other number if necesary. QUESTION WORDING BAD. INDEX AS IN WHEN IT SHOWS UP IN POINTS ARRAY UGHHHHHH EARLIER THE BETTER L to R
        def manhat(a, b):
            return abs(a - x) + abs(b - y)

        for index, value in enumerate(points):
            a, b = value
            dist = manhat(a, b)
            if a == x or b == y:
                if dist < Mdist:
                    Mdist = dist
                    point = index

        return point if point != inf else -1