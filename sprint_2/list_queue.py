import sys


class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class ListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            head_node = self.head
            new_node = Node(value, head_node)
            head_node.prev = new_node
            self.head = new_node

        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            tail_node = self.tail
            self.tail = tail_node.prev
            self.size -= 1
            return tail_node.value

    def is_empty(self):
        return self.tail is None


class CommandHandler:

    def __init__(self):
        self.list_queue = ListQueue()

    def handle_command(self, command):
        if command == 'get':
            self.handle_get_command()
        elif command == 'size':
            self.handle_size_command()
        elif command.find('put') != -1:
            self.handle_put_command(command)

    def handle_get_command(self):
        if self.list_queue.is_empty():
            print('error')
        else:
            print(self.list_queue.pop())

    def handle_size_command(self):
        print(self.list_queue.size)

    def handle_put_command(self, command):
        try:
            number = int(command.split()[1])
            self.list_queue.push(number)
        except ValueError:
            pass


def main():
    command_handler = CommandHandler()
    command_count = int(sys.stdin.readline().strip())

    while command_count:
        command = sys.stdin.readline().strip()
        command_handler.handle_command(command)
        command_count -= 1


if __name__ == '__main__':
    main()
