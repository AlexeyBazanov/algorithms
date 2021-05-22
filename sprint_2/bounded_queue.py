import sys


class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push(self, item):
        if not self.is_full():
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        item = self.queue[self.head]

        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return item

    def peek(self):
        return self.queue[self.head]


class CommandHandler:
    def __init__(self, queue_size):
        self.queue = Queue(queue_size)

    def handle_command(self, command):
        if command == 'pop':
            self.handle_pop_command()
        elif command == 'peek':
            self.handle_peek_command()
        elif command == 'size':
            self.handle_size_command()
        elif command.find('push') != -1:
            self.handle_push_command(command)

    def handle_size_command(self):
        print(self.queue.size)

    def handle_pop_command(self):
        print(self.queue.pop())

    def handle_peek_command(self):
        print(self.queue.peek())

    def handle_push_command(self, command):
        try:
            if self.queue.is_full():
                print('error')
            else:
                number = int(command.split()[1])
                self.queue.push(number)
        except ValueError:
            pass


def main():
    command_count = int(sys.stdin.readline().strip())
    queue_size = int(sys.stdin.readline().strip())
    command_handler = CommandHandler(queue_size)

    while command_count:
        command = sys.stdin.readline().strip()
        command_handler.handle_command(command)
        command_count -= 1


if __name__ == '__main__':
    main()

