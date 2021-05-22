class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def delete(node, index):
    if index == 0:
        return node.next_item

    prev_node = node
    next_node = node

    prev_index = index - 1
    next_index = index + 1

    while prev_index:
        if not prev_node:
            return node
        prev_node = prev_node.next_item
        prev_index -= 1

    while next_index:
        if not next_node:
            return node
        next_node = next_node.next_item
        next_index -= 1

    prev_node.next_item = next_node

    return node


if __name__ == '__main__':
    first_node = Node('first')
    second_node = Node('second', first_node)
    third_node = Node('third', second_node)
    head_node = Node('head', third_node)

    head_node = delete(head_node, 2)

    while head_node:
        print(head_node.value, end=' -> ' if head_node.next_item else '')
        head_node = head_node.next_item
