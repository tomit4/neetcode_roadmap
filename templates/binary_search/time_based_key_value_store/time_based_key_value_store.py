class TimeMap:

    def __init__(self):
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        return None

    def get(self, key: str, timestamp: int) -> str:
        return ""


if __name__ == "__main__":
    time_map: TimeMap = TimeMap()
    time_map.set(key="foo", value="bar", timestamp=1)
    param_1 = time_map.get(key="foo", timestamp=1)
    print(param_1)
    assert param_1 == "bar"
    param_2 = time_map.get(key="foo", timestamp=3)
    print(param_2)
    assert param_2 == "bar"
    time_map.set(key="foo", value="bar2", timestamp=4)
    param_3 = time_map.get(key="foo", timestamp=4)
    print(param_3)
    assert param_3 == "bar2"

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
