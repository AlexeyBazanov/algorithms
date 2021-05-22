class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_index_by_value(node, value):
    index = 0

    while node:
        if node.value == value:
            return index
        node = node.next_item
        index += 1

    return -1


if __name__ == '__main__':
    first_node = Node('first')
    second_node = Node('second', first_node)
    third_node = Node('third', second_node)
    head_node = Node('head', third_node)

    index = get_index_by_value(head_node, 'foo')

    print(index)
