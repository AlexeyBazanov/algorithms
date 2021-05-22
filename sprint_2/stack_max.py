import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1] if self.size() > 0 else None


class StackMax:
    def __init__(self):
        self.items = Stack()
        self.max_values = Stack()

    def push(self, item):
        self.items.push(item)
        self.push_max_value(item)

    def pop(self):
        item = self.items.pop()
        self.pop_max_value(item)
        return item

    def size(self):
        return self.items.size()

    def max(self):
        return self.max_values.peek()

    def push_max_value(self, item):
        if self.max_values.peek() is None or self.max_values.peek() <= item:
            self.max_values.push(item)
            
    def pop_max_value(self, item):
        if item == self.max_values.peek():
            self.max_values.pop()


class CommandHandler:
    def __init__(self):
        self.stack_max = StackMax()

    def handle_command(self, command):
        if command == 'pop':
            self.handle_pop_command()
        elif command == 'get_max':
            self.handle_get_max_command()
        elif command.find('push') != -1:
            self.handle_push_command(command)

    def handle_get_max_command(self):
        print(self.stack_max.max())

    def handle_pop_command(self):
        if self.stack_max.size() > 0:
            self.stack_max.pop()
        else:
            print('error')

    def handle_push_command(self, command):
        try:
            number = int(command.split()[1])
            self.stack_max.push(number)
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



