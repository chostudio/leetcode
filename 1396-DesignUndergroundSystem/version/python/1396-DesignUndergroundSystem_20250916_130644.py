# Last updated: 9/16/2025, 1:06:44 PM
class UndergroundSystem:
    from collections import defaultdict
    def __init__(self):
        self.checkinout = defaultdict(list)
        self.stations = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinout[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkinout[id]
        if (startStation, stationName) in self.stations:
            totalTime, totalPeople = self.stations[(startStation, stationName)]
            totalTime += t - startTime
            totalPeople += 1
            self.stations[(startStation, stationName)] = [totalTime, totalPeople]

        else:
            self.stations[(startStation, stationName)] = [t - startTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.stations:
            totalTime, totalPeople = self.stations[(startStation, endStation)]
            return totalTime / totalPeople


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)