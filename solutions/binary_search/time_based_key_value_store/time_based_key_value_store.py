class TimeMap:

    def __init__(self):
        self.store = {}  # key : list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search
        left: int = 0
        right: int = len(values) - 1

        while left <= right:
            mid: int = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == "__main__":
    time_map: TimeMap = TimeMap()
    time_map.set(key="foo", value="bar", timestamp=1)
    param_1 = time_map.get(key="foo", timestamp=1)
    print("param_1 :=>", param_1)
    param_2 = time_map.get(key="foo", timestamp=3)
    print("param_2 :=>", param_2)
    time_map.set(key="foo", value="bar2", timestamp=4)
    param_3 = time_map.get(key="foo", timestamp=4)
    print("param_3 :=>", param_3)
    param_4 = time_map.get(key="foo", timestamp=5)
    print("param_4 :=>", param_4)

    time_map_2: TimeMap = TimeMap()
    time_map_2.set(key="love", value="high", timestamp=10)
    time_map_2.set(key="love", value="low", timestamp=20)
    param_4 = time_map_2.get(key="love", timestamp=5)
    print(param_4)
    assert param_4 == ""
    param_5 = time_map_2.get(key="love", timestamp=10)
    print(param_5)
    assert param_5 == "high"
    param_6 = time_map_2.get(key="love", timestamp=15)
    print(param_6)
    assert param_6 == "high"
    param_7 = time_map_2.get(key="love", timestamp=20)
    print(param_7)
    assert param_7 == "low"
    param_8 = time_map_2.get(key="love", timestamp=25)
    print(param_8)
    assert param_8 == "low"
