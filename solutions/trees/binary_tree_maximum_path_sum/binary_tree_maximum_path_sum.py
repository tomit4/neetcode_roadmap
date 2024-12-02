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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res: List[int] = [root.val]

        def depth_first_search(root) -> int:
            if not root:
                return 0

            left_max = depth_first_search(root.left)
            right_max = depth_first_search(root.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        depth_first_search(root)
        return res[0]


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[1, 2, 3])
    max_path_sum_1 = solution.maxPathSum(tree_as_list_1)
    print(max_path_sum_1)
    assert max_path_sum_1 == 6

    tree_as_list_2 = convert_list_to_tree(arr=[-10, 9, 20, None, None, 15, 7])
    max_path_sum_2 = solution.maxPathSum(tree_as_list_2)
    print(max_path_sum_2)
    assert max_path_sum_2 == 42
