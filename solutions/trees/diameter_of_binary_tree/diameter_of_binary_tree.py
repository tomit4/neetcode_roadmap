from typing import Dict, List, Optional, Tuple, Union


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


class Solution_5:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack: List[Tuple[Optional[TreeNode], bool]] = [(root, True)]
        diameter = 0
        heights: Dict[Optional[TreeNode], int] = {}

        while stack:
            node, state = stack.pop()

            if not node:
                continue

            if state:
                stack.append((node, False))
                stack.append((node.left, True))  # type:ignore
                stack.append((node.right, True))  # type:ignore
            else:
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)
                node_height = 1 + max(left_height, right_height)
                heights[node] = node_height
                diameter = max(diameter, left_height + right_height)

        return diameter


class Solution_1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0

            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            height = 1 + max(left_height, right_height)
            diameter = max(left_diameter, right_diameter, left_height + right_height)

            return height, diameter

        return dfs(root)[1]


class Solution_2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            # if this doesn't exist(there wasn't an edge here),
            # decrement the res count
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            # return 2 edges if both nodes exist, otherwise return 1 or 0
            res = max(res, 2 + left + right)
            # add 1 edge to the total
            return 1 + max(left, right)

        dfs(root)
        return res


# Note: Similar to above, but more readable and understandable due to use of
# self.diameter instead of res and more intuitive math
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[1, 2, 3, 4, 5])
    diameter_of_binary_tree_1 = solution.diameterOfBinaryTree(tree_as_list_1)
    print(diameter_of_binary_tree_1)
    assert diameter_of_binary_tree_1 == 3

    tree_as_list_2 = convert_list_to_tree(arr=[1, 2])
    diameter_of_binary_tree_2 = solution.diameterOfBinaryTree(tree_as_list_2)
    print(diameter_of_binary_tree_2)
    assert diameter_of_binary_tree_2 == 1

    tree_as_list_3 = convert_list_to_tree(arr=[1])
    diameter_of_binary_tree_3 = solution.diameterOfBinaryTree(tree_as_list_3)
    print(diameter_of_binary_tree_3)
    assert diameter_of_binary_tree_3 == 0

    tree_as_list_4 = convert_list_to_tree(
        arr=[
            4,
            -7,
            -3,
            None,
            None,
            -9,
            -3,
            9,
            -7,
            -4,
            None,
            6,
            None,
            -6,
            -6,
            None,
            None,
            0,
            6,
            5,
            None,
            9,
            None,
            None,
            -1,
            -4,
            None,
            None,
            None,
            -2,
        ]
    )
    diameter_of_binary_tree_4 = solution.diameterOfBinaryTree(tree_as_list_4)
    print(diameter_of_binary_tree_4)
    assert diameter_of_binary_tree_4 == 8
