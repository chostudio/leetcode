# Last updated: 9/11/2025, 12:31:27 PM
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append((price ,1))
            return 1
        else: # something in the stack
            count = 1
            while len(self.stack) > 0 and self.stack[-1][0] <= price:
                count += self.stack[-1][1]
                self.stack.pop()
            self.stack.append((price, count))
            return self.stack[-1][1]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)