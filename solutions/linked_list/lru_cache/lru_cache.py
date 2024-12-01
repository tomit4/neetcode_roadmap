from typing import Dict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap: int = capacity
        self.cache: Dict[int, Node] = {}  # map key to node

        self.left: Node = Node(0, 0)
        self.right: Node = Node(0, 0)

        # left = LRU, right = most recent
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node) -> None:
        prev: Node = node.prev
        nxt: Node = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at right
    def insert(self, node) -> None:
        prev: Node | None = self.right.prev
        nxt: Node | None = self.right
        prev.next = node  # type:ignore
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete/evict the LRU from the hashmap
            lru: Node | None = self.left.next
            self.remove(lru)
            del self.cache[lru.key]  # type: ignore


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
