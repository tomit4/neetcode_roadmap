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


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res: List[int] = [0]

        def depth_first_search(root) -> int:
            if not root:
                return -1  # accounts for null node
            left: int = depth_first_search(root.left)  # finds height of left subtree
            right: int = depth_first_search(root.right)  # finds height of right subtree

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        depth_first_search(root)
        return res[0]


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
