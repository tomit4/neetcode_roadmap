class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        return

    def get(self, key: int) -> int:
        return 0

    def put(self, key: int, value: int) -> None:
        return


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
