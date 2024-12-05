class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.end_word = True

    def search(self, word: str) -> bool:
        def depth_first_search(j: int, root: TrieNode) -> bool:
            cur: TrieNode = root

            for i in range(j, len(word)):
                c: str = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if depth_first_search(i + 1, child):
                            return True
                        return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.end_word

        return depth_first_search(j=0, root=self.root)


if __name__ == "__main__":
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print(word_dict.search("pad"))
    assert word_dict.search("pad") == False
    print(word_dict.search("bad"))
    assert word_dict.search("bad") == True
    print(word_dict.search(".ad"))
    assert word_dict.search(".ad") == True
    print(word_dict.search("b.."))
    assert word_dict.search("b..") == True
