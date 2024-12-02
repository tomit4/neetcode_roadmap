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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


if __name__ == "__main__":
    solution = Solution()
    preorder_1 = arr = [3, 9, 20, 15, 7]
    inorder_1 = arr = [9, 3, 15, 20, 7]
    build_tree_1 = solution.buildTree(preorder=preorder_1, inorder=inorder_1)
    print(convert_tree_to_list(build_tree_1))
    assert convert_tree_to_list(build_tree_1) == [3, 9, 20, None, None, 15, 7]

    preorder_2 = arr = [-1]
    inorder_2 = arr = [-1]
    build_tree_2 = solution.buildTree(preorder=preorder_2, inorder=inorder_2)
    print(convert_tree_to_list(build_tree_2))
    assert convert_tree_to_list(build_tree_2) == [-1]
