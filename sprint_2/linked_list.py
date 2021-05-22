class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


def insert_node(head, index, value):
    new_node = Node(value)

    if index == 0:
        new_node.prev = head
        return new_node

    previous_node = get_node_by_index(head, index-1)
    new_node.prev = previous_node.prev
    previous_node.prev = new_node

    return head


def get_node_by_index(node, index):
    while index:
        node = node.prev
        index -= 1
    return node


def main():
    first_node = Node('first')
    second_node = Node('second', first_node)
    third_node = Node('third', second_node)
    head_node = Node('head', third_node)

    # node = get_node_by_index(head_node, 3)
    #
    # print(node.value)

    head_node = insert_node(head_node, 4, 'new_node')

    while head_node:
        print(head_node.value, end=' -> ' if head_node.prev else '')
        head_node = head_node.prev

    print()


main()
