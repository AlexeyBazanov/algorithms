class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def search_node(root, key, parent=None):
    if root is None:
        return None, None
    if root.value == key:
        return root, parent
    if root.value > key:
        return search_node(root.left, key, root)
    else:
        return search_node(root.right, key, root)


def replace_child(parent, prev_child, new_child):
    if parent is None or prev_child is None:
        return
    if parent.left and parent.left.value == prev_child.value:
        parent.left = new_child
    elif parent.right and parent.right.value == prev_child.value:
        parent.right = new_child


def reconnect_bounds(parent, node):
    if node.left:
        replace_child(parent, node, node.left)
    elif node.right:
        replace_child(parent, node, node.right)
    else:
        replace_child(parent, node, None)


def get_substitute(node, parent):
    if node.left:
        parent = node
        node = node.left
        while node.right:
            parent = node
            node = node.right

    elif node.right:
        parent = node
        node = node.right
        while node.left:
            parent = node
            node = node.left

    return node, parent


def remove(root, key):
    if root is None:
        return None

    deleted, deleted_parent = search_node(root, key)

    # If node with searched key wasn't found
    if deleted is None:
        return root

    # If root without leaves was deleted
    if deleted_parent is None and deleted.left is None and deleted.right is None:
        return None

    substitute, substitute_parent = get_substitute(deleted, deleted_parent)

    replace_child(deleted_parent, deleted, substitute)

    if substitute is None:
        return root

    reconnect_bounds(substitute_parent, substitute)

    substitute.left = deleted.left
    substitute.right = deleted.right

    if deleted_parent is None:
        root = substitute

    return root


def display(root):
    if root is None:
        print(None)
        return
    lines, *_ = display_aux(root)
    for line in lines:
        print(line)


def display_aux(root):
    if root.right is None and root.left is None:
        line = '%s' % root.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = display_aux(root.left)
        s = '%s' % root.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = display_aux(root.right)
        s = '%s' % root.value
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display_aux(root.left)
    right, m, q, y = display_aux(root.right)
    s = '%s' % root.value
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def test():
    # node1 = Node(None, None, 2)
    # node2 = Node(node1, None, 3)
    # node3 = Node(None, node2, 1)
    # node4 = Node(None, None, 6)
    # node5 = Node(node4, None, 8)
    # node6 = Node(node5, None, 10)
    # node7 = Node(node3, node6, 5)
    # newHead = remove(node7, 10)
    # assert newHead.value == 5
    # assert newHead.right is node5
    # assert newHead.right.value == 8


    # node1 = Node(None, None, 1)
    # node3 = Node(None, None, 3)
    # node2 = Node(node1, node3, 2)
    #
    # node5 = Node(None, None, 5)
    # node66 = Node(None, None, 66)
    # node7 = Node(node66, None, 7)
    # node6 = Node(node5, node7, 6)
    #
    # node4 = Node(node2, node6, 4)
    #
    # node9 = Node(None, None, 9)
    # node12 = Node(None, None, 12)
    # node10 = Node(node9, node12, 10)
    #
    # node13 = Node(None, None, 13)
    # node15 = Node(None, None, 15)
    # node14 = Node(node13, node15, 14)
    #
    # node11 = Node(node10, node14, 11)
    #
    # node8 = Node(node4, node11, 8)
    #
    # display(node8)
    #
    # root = remove(node8, 4)
    #
    # display(root)

    node7 = Node(None, None, 7)
    node5 = Node(None, node7, 5)
    node10 = Node(node5, None, 10)

    # display(node10)

    root = remove(node10, 10)

    display(root)


test()