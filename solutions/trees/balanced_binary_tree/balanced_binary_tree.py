from typing import List, Optional, Tuple, Union


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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth_first_search(root) -> Tuple[bool, int]:
            if not root:
                return (True, 0)

            left = depth_first_search(root.left)
            right = depth_first_search(root.right)

            # left[0] is balanced(True)
            # right [0] is balanced(True)
            # height thus far is leq 1
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            height = 1 + max(left[1], right[1])

            return (balance, height)

        return depth_first_search(root)[0]


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[3, 9, 20, None, None, 15, 7])
    is_tree_balanced_1 = solution.isBalanced(tree_as_list_1)
    print(is_tree_balanced_1)
    assert is_tree_balanced_1 == True

    tree_as_list_2 = convert_list_to_tree(arr=[1, 2, 2, 3, 3, None, None, 4, 4])
    is_tree_balanced_2 = solution.isBalanced(tree_as_list_2)
    print(is_tree_balanced_2)
    assert is_tree_balanced_2 == False

    tree_as_list_3 = convert_list_to_tree(arr=[])
    is_tree_balanced_3 = solution.isBalanced(tree_as_list_3)
    print(is_tree_balanced_3)
    assert is_tree_balanced_3 == True
