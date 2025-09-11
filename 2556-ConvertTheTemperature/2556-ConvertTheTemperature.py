# Last updated: 9/11/2025, 12:30:39 PM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = [0,0]
        ans[0] = celsius + 273.15
        ans[1] = celsius * 1.80 + 32.00
        return ans