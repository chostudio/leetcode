# Last updated: 2/8/2026, 12:44:05 PM
1class MyHashSet:
2
3    def __init__(self):
4        self.set = [False] * (10**6 + 1)
5
6    def add(self, key: int) -> None:
7        self.set[key] = True
8
9    def remove(self, key: int) -> None:
10        self.set[key] = False
11
12    def contains(self, key: int) -> bool:
13        return self.set[key]
14
15
16# Your MyHashSet object will be instantiated and called as such:
17# obj = MyHashSet()
18# obj.add(key)
19# obj.remove(key)
20# param_3 = obj.contains(key)