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


if __name__ == "__main__":
    obj = MinStack()
    obj.push(val=-2)
    obj.push(val=0)
    obj.push(val=-3)
    min_1 = obj.getMin()
    print(min_1)
    assert min_1 == -3
    obj.pop()
    top = obj.top()
    print(top)
    assert top == 0
    min_2 = obj.getMin()
    print(min_2)
    assert min_2 == -2
