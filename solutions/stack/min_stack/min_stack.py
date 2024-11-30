class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    obj = MinStack()
    obj.push(val=-2)
    obj.push(val=0)
    obj.push(val=-3)
    obj.pop()
    param_3: int = obj.top()
    print("param_3 :=> ", param_3)
    param_4: int = obj.getMin()
    print("param_4 :=> ", param_4)
