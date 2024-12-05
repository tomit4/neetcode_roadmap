from typing import List, Set


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        ROWS: int = len(board)
        COLS: int = len(board[0])
        res: Set = set()
        visit: Set = set()

        def depth_first_search(
            row: int, col: int, node: TrieNode, word: str
        ) -> List[str] | None:
            if (
                row < 0
                or col < 0
                or row == ROWS
                or col == COLS
                or (row, col) in visit
                or board[row][col] not in node.children
            ):
                return

            visit.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.is_word:
                res.add(word)

            depth_first_search(row - 1, col, node, word)
            depth_first_search(row + 1, col, node, word)
            depth_first_search(row, col - 1, node, word)
            depth_first_search(row, col + 1, node, word)

            visit.remove((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                depth_first_search(row, col, root, "")

        return list(res)


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findWords(
            board=[
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            words=["oath", "pea", "eat", "rain"],
        )
    )
    # NOTE: Cast to `set` since it can output both words in either order
    assert set(
        solution.findWords(
            board=[
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            words=["oath", "pea", "eat", "rain"],
        )
    ) == {"eat", "oath"}
    print(solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))
    assert solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]) == []
