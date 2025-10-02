# Last updated: 10/1/2025, 7:58:05 PM
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] # keep track of smallest at that moment

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            # BE WARY OF NAMING minstack vs stack in places here
            self.minstack.append(min(self.minstack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()