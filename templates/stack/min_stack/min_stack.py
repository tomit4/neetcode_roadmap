class MinStack:

    def __init__(self):
        return None

    def push(self, val: int) -> None:
        return None

    def pop(self) -> None:
        return None

    def top(self) -> int:
        return 0

    def getMin(self) -> int:
        return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    obj = MinStack()
    obj.push(val=1)
    obj.push(val=2)
    obj.push(val=3)
    obj.pop()
    param_3: int = obj.top()
    print("param_3 :=> ", param_3)
    param_4: int = obj.getMin()
    print("param_4 :=> ", param_4)
