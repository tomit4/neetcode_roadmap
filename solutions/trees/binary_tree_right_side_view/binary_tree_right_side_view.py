from collections import deque
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []
        queue: deque = deque([root])

        # Another Breath First Search Solution
        # Just keeps track of the right side node throughout traversal
        # and stores it in the res list
        while queue:
            right_side: Optional[TreeNode] = None
            queue_len: int = len(queue)

            for _ in range(queue_len):
                node: TreeNode = queue.popleft()
                if node:
                    right_side = node
                    queue.append(node.left)  # must add left node before right node
                    queue.append(node.right)

            if right_side:
                res.append(right_side.val)

        return res


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[1, 2, 3, None, 5, None, 4])
    right_side_view_1 = solution.rightSideView(tree_as_list_1)
    print(right_side_view_1)
    assert right_side_view_1 == [1, 3, 4]

    tree_as_list_2 = convert_list_to_tree(arr=[1, 2, 3, 4, None, None, None, 5])
    right_side_view_2 = solution.rightSideView(tree_as_list_2)
    print(right_side_view_2)
    assert right_side_view_2 == [1, 3, 4, 5]

    tree_as_list_3 = convert_list_to_tree(arr=[1, None, 3])
    right_side_view_3 = solution.rightSideView(tree_as_list_3)
    print(right_side_view_3)
    assert right_side_view_3 == [1, 3]

    tree_as_list_4 = convert_list_to_tree(arr=[])
    right_side_view_4 = solution.rightSideView(tree_as_list_4)
    print(right_side_view_4)
    assert right_side_view_4 == []
