from collections import deque
from typing import Tuple


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinaryTree:
    def __init__(self) -> None:
        pass

    def _get_successor(self, root: TreeNode) -> Tuple[TreeNode | None, TreeNode]:
        current = root
        parent = None
        while current.left:
            parent = current
            current = current.left
        return parent, current

    def insert(self, root: TreeNode | None, value: int) -> TreeNode:
        if not root:
            root = TreeNode(value)
            return root

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def delete(self, root: TreeNode | None, value: int) -> TreeNode | None:
        if not root:
            return None

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left and root.right:
                parent_successor, successor = self._get_successor(root.right)
                if parent_successor:
                    parent_successor.left = successor.right
                else:
                    root.right = successor.right
                successor.left = root.left
                successor.right = root.right
                return successor

            return root.left if root.left else root.right

        return root

    def search(self, root: TreeNode | None, value: int) -> bool:
        if not root:
            return False
        elif root.value == value:
            return True
        elif root.value < value:
            return self.search(root.right, value)
        else:
            return self.search(root.left, value)

    def find_max(self, root: TreeNode | None) -> int | float:
        if not root:
            return float("-inf")

        elif root.right == None:
            return root.value
        else:
            return self.find_max(root.right)

    def find_min(self, root: TreeNode | None) -> int | float:
        if not root:
            return float("-inf")

        elif root.left == None:
            return root.value
        else:
            return self.find_min(root.left)

    def in_order_traversal(self, root: TreeNode | None) -> None:
        if root:
            self.in_order_traversal(root.left)
            print(root.value, end=" -> ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root: TreeNode | None) -> None:
        if root:
            print(root.value, end=" -> ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root: TreeNode | None) -> None:
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.value, end=" -> ")

    def level_order_traversal(self, root: TreeNode | None) -> None:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            print(node.value, end=" -> ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def get_height(self, root: TreeNode | None) -> int:
        if not root:
            return -1

        height = 1
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        return height + max(left_height, right_height)

    def is_balanced(self, root: TreeNode | None) -> bool:
        def check_height(node: TreeNode | None) -> int:
            if not node:
                return 0

            left_height = check_height(node.left)
            right_height = check_height(node.right)

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return check_height(root) != -1

    def is_full(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        if (not root.left and root.right) or (root.left and not root.right):
            return False

        return self.is_full(root.left) and self.is_full(root.right)

    def count_nodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        count = 1
        count += self.count_nodes(root.left)
        count += self.count_nodes(root.right)

        return count

    def count_leaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left_count = self.count_leaves(root.left)
        right_count = self.count_leaves(root.right)

        return left_count + right_count

    def invert(self, root: TreeNode | None) -> TreeNode | None:
        if root:
            root.left, root.right = self.invert(root.right), self.invert(root.left)
        return root

    def diameter(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> Tuple[int, int]:
            if not node:
                return 0, 0

            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            height = 1 + max(left_height, right_height)
            diameter = max(left_diameter, right_diameter, left_height + right_height)

            return height, diameter

        return dfs(root)[1]

    def lowest_common_ancestor(
        self, root: TreeNode | None, p: int, q: int
    ) -> TreeNode | None:
        if not root or root.value == p or root.value == q:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right

    def has_path_sum(self, root: TreeNode | None, target_sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return target_sum == root.value

        left_has_path_sum = self.has_path_sum(root.left, target_sum - root.value)
        right_has_path_sum = self.has_path_sum(root.right, target_sum - root.value)
        return left_has_path_sum or right_has_path_sum


if __name__ == "__main__":
    binary_tree = BinaryTree()
    root = None

    # Insert values into the binary tree
    values_to_insert = [15, 10, 20, 8, 12, 17, 25]
    for value in values_to_insert:
        root = binary_tree.insert(root, value)

    # Display the tree structure
    print("Tree after insertion:")
    print("In-order traversal:")
    binary_tree.in_order_traversal(root)
    print("\nPre-order traversal:")
    binary_tree.pre_order_traversal(root)
    print("\nPost-order traversal:")
    binary_tree.post_order_traversal(root)
    print("\nLevel-order traversal:")
    binary_tree.level_order_traversal(root)
    print()

    # Display min and max values
    print("Min value :=>", binary_tree.find_min(root))
    print("Max value :=>", binary_tree.find_max(root))

    # Search for values
    print("Searching for 10 :=>", binary_tree.search(root, 10))
    print("Searching for 99 :=>", binary_tree.search(root, 99))

    # Delete a value and display the tree again
    root = binary_tree.delete(root, 10)
    print("\nTree after deleting 10:")
    print("In-order traversal:")
    binary_tree.in_order_traversal(root)
    print("\nPre-order traversal:")
    binary_tree.pre_order_traversal(root)
    print("\nPost-order traversal:")
    binary_tree.post_order_traversal(root)
    print("\nLevel-order traversal:")
    binary_tree.level_order_traversal(root)
    print()

    print("\nMin value :=>", binary_tree.find_min(root))
    print("Max value :=>", binary_tree.find_max(root))
    print("Searching for 10 :=>", binary_tree.search(root, 10))

    # Assert statements for correctness
    assert binary_tree.search(root, 8) == True
    assert binary_tree.search(root, 10) == False
    assert binary_tree.find_min(root) == 8
    assert binary_tree.find_max(root) == 25
    assert binary_tree.is_full(root) == False
    assert binary_tree.count_nodes(root) == 6
    assert binary_tree.count_leaves(root) == 3
    assert binary_tree.is_balanced(root) == True

    # Height and diameter
    print("\nHeight of the tree:", binary_tree.get_height(root))
    print("Diameter of the tree:", binary_tree.diameter(root))
    assert binary_tree.get_height(root) == 2
    assert binary_tree.diameter(root) == 4

    # Invert the tree and display again
    root = binary_tree.invert(root)
    print("\nTree after inversion:")
    print("In-order traversal:")
    binary_tree.in_order_traversal(root)
    print("\nPre-order traversal:")
    binary_tree.pre_order_traversal(root)
    print("\nPost-order traversal:")
    binary_tree.post_order_traversal(root)
    print("\nLevel-order traversal:")
    binary_tree.level_order_traversal(root)
    print()

    print("\nPre-order traversal after inversion:")
    print("In-order traversal:")
    binary_tree.in_order_traversal(root)
    print("\nPre-order traversal:")
    binary_tree.pre_order_traversal(root)
    print("\nPost-order traversal:")
    binary_tree.post_order_traversal(root)
    print("\nLevel-order traversal:")
    binary_tree.level_order_traversal(root)
    print()

    # LCA test
    print("\nLowest Common Ancestor of 17 and 25:")
    lca_node = binary_tree.lowest_common_ancestor(root, 17, 25)
    print("LCA value:", lca_node.value if lca_node else "None")
    if lca_node:
        assert lca_node.value == 20

    # Path sum test
    print("\nDoes a path sum of 32 exist?:", binary_tree.has_path_sum(root, 32))
    print("Does a path sum of 50 exist?:", binary_tree.has_path_sum(root, 50))
    assert binary_tree.has_path_sum(root, 32) == False
    assert binary_tree.has_path_sum(root, 50) == False

    print("\nAll tests passed!")
