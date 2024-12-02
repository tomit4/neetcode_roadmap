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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        # recursive depth first search solution
        if not root:
            return 0

        def depth_first_search(node, max_val) -> int:
            if not node:
                return 0

            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            res += depth_first_search(node.left, max_val)
            res += depth_first_search(node.right, max_val)
            return res

        return depth_first_search(root, root.val)


if __name__ == "__main__":
    solution = Solution()
    tree_as_list_1 = convert_list_to_tree(arr=[3, 1, 4, 3, None, 1, 5])
    good_nodes_1 = solution.goodNodes(tree_as_list_1)
    print(good_nodes_1)
    assert good_nodes_1 == 4

    tree_as_list_2 = convert_list_to_tree(arr=[3, 3, None, 4, 2])
    good_nodes_2 = solution.goodNodes(tree_as_list_2)
    print(good_nodes_2)
    assert good_nodes_2 == 3

    tree_as_list_3 = convert_list_to_tree(arr=[1])
    good_nodes_3 = solution.goodNodes(tree_as_list_3)
    print(good_nodes_3)
    assert good_nodes_3 == 1
