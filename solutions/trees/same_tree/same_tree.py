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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[1, 2, 3])
    tree_as_list_2 = convert_list_to_tree(arr=[1, 2, 3])
    is_tree_same_1 = solution.isSameTree(tree_as_list_1, tree_as_list_2)
    print(is_tree_same_1)
    assert is_tree_same_1 == True

    tree_as_list_3 = convert_list_to_tree(arr=[1, 2])
    tree_as_list_4 = convert_list_to_tree(arr=[1, None, 2])
    is_tree_same_2 = solution.isSameTree(tree_as_list_3, tree_as_list_4)
    print(is_tree_same_2)
    assert is_tree_same_2 == False

    tree_as_list_5 = convert_list_to_tree(arr=[1, 2, 1])
    tree_as_list_6 = convert_list_to_tree(arr=[1, 1, 2])
    is_tree_same_3 = solution.isSameTree(tree_as_list_5, tree_as_list_6)
    print(is_tree_same_3)
    assert is_tree_same_3 == False
