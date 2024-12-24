from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_tree(root: TreeNode | None):
    if not root:
        return  # Empty tree

    queue = deque([root])  # Queue for BFS

    while queue:
        node = queue.popleft()  # Dequeue the front node
        print(f"Visiting node with value {node.val}")

        # Add children to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Example problem
# Problem: Find the level order traversal of a binary tree


def level_order(root: TreeNode | None) -> List[TreeNode]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
