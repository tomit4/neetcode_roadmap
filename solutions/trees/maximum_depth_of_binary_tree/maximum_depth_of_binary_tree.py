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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive Depth First Search
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[3, 9, 20, None, None, 15, 7])
    max_depth_of_tree_1 = solution.maxDepth(tree_as_list_1)
    print(max_depth_of_tree_1)
    assert max_depth_of_tree_1 == 3

    tree_as_list_2 = convert_list_to_tree(arr=[1, None, 2])
    max_depth_of_tree_2 = solution.maxDepth(tree_as_list_2)
    print(max_depth_of_tree_2)
    assert max_depth_of_tree_2 == 2
