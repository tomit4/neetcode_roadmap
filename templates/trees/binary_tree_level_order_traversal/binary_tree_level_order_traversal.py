from typing import List, Optional, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_list_to_tree(arr: List[Union[int, None]]) -> Optional[TreeNode]:
    """
    Converts a list representation of a binary tree
    into an actual TreeNode-based binary tree.
    """
    if not arr:
        return None

    # Create a list of TreeNode objects (or None for nulls)
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    kids = nodes[::-1]  # Reverse to pop nodes from the end
    root = kids.pop()  # The root is the last item in the reversed list

    # Assign children to nodes level by level
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


def convert_tree_to_list(root: Optional[TreeNode]) -> List[Union[int, None]]:
    """
    Converts a TreeNode-based binary tree into its list representation.
    """
    if not root:
        return []

    result = []
    queue: List[Optional[TreeNode]] = [root]  # Use a queue for level-order traversal

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return [[]]


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[3, 9, 20, None, None, 15, 7])
    level_order_1 = solution.levelOrder(tree_as_list_1)
    print(level_order_1)
    assert level_order_1 == [[3], [9, 20], [15, 7]]

    tree_as_list_2 = convert_list_to_tree(arr=[1])
    level_order_2 = solution.levelOrder(tree_as_list_2)
    print(level_order_2)
    assert level_order_2 == [[1]]

    tree_as_list_3 = convert_list_to_tree(arr=[])
    level_order_3 = solution.levelOrder(tree_as_list_3)
    print(level_order_3)
    assert level_order_3 == []
