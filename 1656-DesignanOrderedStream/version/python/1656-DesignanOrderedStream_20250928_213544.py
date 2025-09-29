# Last updated: 9/28/2025, 9:35:44 PM
class OrderedStream:
    from collections import defaultdict
    def __init__(self, n: int):
        self.map = defaultdict(str)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.map[idKey] = value
        ans = []
        while self.ptr in self.map:
            ans.append(self.map[self.ptr])
            self.ptr += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)