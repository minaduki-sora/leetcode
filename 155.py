class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append((val, min(val, self.s[-1][1]) if self.s else val))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()