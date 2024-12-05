class Trie:

    def __init__(self):
        return

    def insert(self, word: str) -> None:
        return

    def search(self, word: str) -> bool:
        return True

    def startsWith(self, prefix: str) -> bool:
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True
