class WordDictionary:

    def __init__(self):
        return

    def addWord(self, word: str) -> None:
        return

    def search(self, word: str) -> bool:
        return True


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
