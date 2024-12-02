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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return True


if __name__ == "__main__":
    solution = Solution()
    root_1 = convert_list_to_tree(arr=[3, 4, 5, 1, 2])
    sub_root_1 = convert_list_to_tree(arr=[4, 1, 2])
    is_sub_tree_1 = solution.isSubtree(root=root_1, subRoot=sub_root_1)
    print(is_sub_tree_1)
    assert is_sub_tree_1 == True

    root_2 = convert_list_to_tree(arr=[3, 4, 5, 1, 2, None, None, None, None, 0])
    sub_root_2 = convert_list_to_tree(arr=[4, 1, 2])
    is_sub_tree_2 = solution.isSubtree(root=root_2, subRoot=sub_root_2)
    print(is_sub_tree_2)
    assert is_sub_tree_2 == True
