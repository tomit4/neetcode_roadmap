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


class Solution_recursive:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))


class Solution_iterative:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, left, right = stack.pop()
            if node.val <= left or node.val >= right:
                return False
            if node.left:
                stack.append((node.left, left, node.val))
            if node.right:
                stack.append((node.right, node.val, right))

        return True


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[2, 1, 3])
    is_valid_bst_1 = solution.isValidBST(tree_as_list_1)
    print(is_valid_bst_1)
    assert is_valid_bst_1 == True

    tree_as_list_2 = convert_list_to_tree(arr=[5, 1, 4, None, None, 3, 6])
    is_valid_bst_2 = solution.isValidBST(tree_as_list_2)
    print(is_valid_bst_2)
    assert is_valid_bst_2 == False

    tree_as_list_3 = convert_list_to_tree(arr=[5, 4, 6, None, None, 3, 7])
    is_valid_bst_3 = solution.isValidBST(tree_as_list_3)
    print(is_valid_bst_3)
    assert is_valid_bst_3 == False
