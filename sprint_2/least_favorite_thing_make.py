def solution(node, index):
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
