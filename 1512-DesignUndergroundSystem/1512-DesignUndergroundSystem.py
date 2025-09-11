# Last updated: 9/11/2025, 12:31:07 PM
class UndergroundSystem:

    def __init__(self):
        self.checkInMap = defaultdict(tuple)
        # three hashmap bc store final is easier to do with times by itself and station amount of people by itself too +=
        self.duration = defaultdict(int)
        self.people = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # remember layout
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # grab it
        checkInStation, ogTime = self.checkInMap[id]
        # remove it
        del self.checkInMap[id] # not delete but 'del'
        # store new
        self.duration[(checkInStation, stationName)] += t - ogTime
        self.people[(checkInStation, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #  store it in above way to get o(1) time like this when calc avg
        return self.duration[(startStation, endStation)] / self.people[(startStation, endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)