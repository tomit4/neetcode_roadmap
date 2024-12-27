class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def print_all_leaf_nodes(root: TreeNode | None):
    if not root:
        return

    if not root.left and not root.right:
        print(root.value, end=" ")
        return

    print_all_leaf_nodes(root.left)
    print_all_leaf_nodes(root.right)


print("Leaf nodes:", end=" ")
print_all_leaf_nodes(root)
