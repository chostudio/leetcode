# Last updated: 10/19/2026, 9:22:00 AM
1# list obj not callable error, means there a variable and a funcitno with the same name
2
3class BrowserHistory:
4
5    def __init__(self, homepage: str):
6        self.backward = [homepage]
7        self.forwards = []
8
9    def visit(self, url: str) -> None:
10        self.forwards = []
11        self.backward.append(url)
12
13    def back(self, steps: int) -> str:
14        steps = min(steps, len(self.backward)-1)
15
16        for i in range(steps):
17            self.forwards.append(self.backward.pop())
18        return self.backward[-1]
19
20    def forward(self, steps: int) -> str:
21        steps = min(steps, len(self.forwards))
22
23        for i in range(steps):
24            self.backward.append(self.forwards.pop())
25        return self.backward[-1]
26
27# Your BrowserHistory object will be instantiated and called as such:
28# obj = BrowserHistory(homepage)
29# obj.visit(url)
30# param_2 = obj.back(steps)
31# param_3 = obj.forward(steps)