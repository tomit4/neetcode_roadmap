from collections import deque
from typing import Tuple


class TreeNode:
    def __init__(self, value: int):
        pass


class BinaryTree:
    def __init__(self) -> None:
        pass

    def _get_successor(self, root: TreeNode) -> Tuple[TreeNode | None, TreeNode]:
        pass

    def insert(self, root: TreeNode | None, value: int) -> TreeNode:
        pass

    def delete(self, root: TreeNode | None, value: int) -> TreeNode | None:
        pass

    def search(self, root: TreeNode | None, value: int) -> bool:
        pass

    def find_max(self, root: TreeNode | None) -> int | float:
        pass

    def find_min(self, root: TreeNode | None) -> int | float:
        pass

    def in_order_traversal(self, root: TreeNode | None) -> None:
        pass

    def pre_order_traversal(self, root: TreeNode | None) -> None:
        pass

    def post_order_traversal(self, root: TreeNode | None) -> None:
        pass

    def level_order_traversal(self, root: TreeNode | None) -> None:
        pass

    def get_height(self, root: TreeNode | None) -> int:
        pass

    def is_balanced(self, root: TreeNode | None) -> bool:
        pass

    def is_full(self, root: TreeNode | None) -> bool:
        pass

    def count_nodes(self, root: TreeNode | None) -> int:
        pass

    def count_leaves(self, root: TreeNode | None) -> int:
        pass

    def invert(self, root: TreeNode | None) -> TreeNode | None:
        pass

    def diameter(self, root: TreeNode | None) -> int:
        pass

    def lowest_common_ancestor(
        self, root: TreeNode | None, p: int, q: int
    ) -> TreeNode | None:
        pass

    def has_path_sum(self, root: TreeNode | None, target_sum: int) -> bool:
        pass


if __name__ == "__main__":
    binary_tree = BinaryTree()
    root = None
