class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> bool:
    return is_bst(root)


def is_bst(root: Node, left: Node = None, right: Node = None):
    if root is None:
        return True

    if left is not None and root.value <= left.value:
        return False

    if right is not None and root.value >= right.value:
        return False

    return is_bst(root.left, left, root) and is_bst(root.right, root, right)
