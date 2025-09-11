# Last updated: 9/11/2025, 12:31:30 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zi = zip(position, speed)
        # returns a zip object, which is an iterator of tuples. NOT an array
        # sorted() returns a sorted object, so you need to assign the value to something. unlike .sort() which is a func that sorts the obj calling it. but that's only for arrays and not zip objects

        time = []
        for pos, spe in sorted(zi, reverse=True):
            print(pos, spe)
            dist = target - pos
            # speed = dist / time, m/s
            # time = distance / speed, m/m/s = s (meters cancel out)
            t = dist / spe
            if len(time) == 0 or t > time[-1]:
                time.append(t)

        return len(time)