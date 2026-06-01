# Last updated: 6/1/2026, 12:54:36 PM
1class Solution:
2    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
3        asteroids.sort()
4        for a in asteroids:
5            if a > mass:
6                return False
7            mass += a
8        return True
9