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
    print("param_1 :=>", param_1)
    param_2 = time_map.get(key="foo", timestamp=3)
    print("param_2 :=>", param_2)
    time_map.set(key="foo", value="bar2", timestamp=4)
    param_3 = time_map.get(key="foo", timestamp=4)
    print("param_3 :=>", param_3)
    param_4 = time_map.get(key="foo", timestamp=5)
    print("param_4 :=>", param_4)
