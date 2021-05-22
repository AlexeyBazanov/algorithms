import unittest
from io import StringIO
from unittest.mock import patch
from deque import Deque
from deque import CommandHandler


class TestDeque(unittest.TestCase):

    def test_push_back(self):
        deque = Deque(3)
        deque.push_back(1)
        deque.push_back(2)
        deque.push_back(3)

        self.assertEqual(deque.items(), [1, 2, 3])
        self.assertEqual(deque.tail(), 0)
        self.assertEqual(deque.head(), 0)
        self.assertEqual(deque.size(), 3)

    def test_push_front(self):
        deque = Deque(3)
        deque.push_front(1)
        deque.push_front(2)
        deque.push_front(3)

        self.assertEqual(deque.items(), [3, 2, 1])
        self.assertEqual(deque.head(), 0)
        self.assertEqual(deque.tail(), 0)
        self.assertEqual(deque.size(), 3)

    def test_pop_back(self):
        deque = Deque(3)
        deque.push_back(1)
        deque.push_back(2)
        deque.push_back(3)

        self.assertEqual(deque.pop_back(), 3)
        self.assertEqual(deque.pop_back(), 2)
        self.assertEqual(deque.pop_back(), 1)

        self.assertEqual(deque.size(), 0)

        deque.push_front(1)
        deque.push_front(2)
        deque.push_front(3)

        self.assertEqual(deque.pop_back(), 1)
        self.assertEqual(deque.pop_back(), 2)
        self.assertEqual(deque.pop_back(), 3)

        self.assertEqual(deque.size(), 0)

    def test_pop_front(self):
        deque = Deque(3)
        deque.push_back(1)
        deque.push_back(2)
        deque.push_back(3)

        self.assertEqual(deque.pop_front(), 1)
        self.assertEqual(deque.pop_front(), 2)
        self.assertEqual(deque.pop_front(), 3)

        self.assertEqual(deque.size(), 0)

        deque.push_front(1)
        deque.push_front(2)
        deque.push_front(3)

        self.assertEqual(deque.pop_front(), 3)
        self.assertEqual(deque.pop_front(), 2)
        self.assertEqual(deque.pop_front(), 1)

        self.assertEqual(deque.size(), 0)

    def test_many_value(self):
        push_to_front = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        push_to_back = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        deque = Deque(20)

        for i in push_to_front:
            deque.push_front(i)

        for i in push_to_back:
            deque.push_back(i)

        for i in range(1, 21):
            self.assertEqual(deque.pop_front(), i)

        for i in push_to_front:
            deque.push_front(i)

        for i in push_to_back:
            deque.push_back(i)

        for i in range(20, 1, -1):
            self.assertEqual(deque.pop_back(), i)

    def test_push_to_full_exception(self):
        deque = Deque(1)
        deque.push_back(1)
        self.assertRaises(IndexError, deque.push_back, 2)
        self.assertRaises(IndexError, deque.push_front, 2)

    def test_pull_from_empty_exception(self):
        deque = Deque(1)
        self.assertRaises(IndexError, deque.pop_back)
        self.assertRaises(IndexError, deque.pop_front)


class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.command_handler = CommandHandler(3)

    def test_push_back_command(self):
        self.command_handler.handle_command('push_back 1')
        self.command_handler.handle_command('push_back 2')
        self.command_handler.handle_command('push_back 3')

        self.assertEqual(self.command_handler.deque.items(), [1, 2, 3])

    def test_push_front_command(self):
        self.command_handler.handle_command('push_front 1')
        self.command_handler.handle_command('push_front 2')
        self.command_handler.handle_command('push_front 3')

        self.assertEqual(self.command_handler.deque.items(), [3, 2, 1])

    def test_pop_back_command(self):
        self.command_handler.handle_command('push_back 1')
        self.command_handler.handle_command('push_back 2')
        self.command_handler.handle_command('push_back 3')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_back')
            self.assertEqual(fakeOutput.getvalue().strip(), '3')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_back')
            self.assertEqual(fakeOutput.getvalue().strip(), '2')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_back')
            self.assertEqual(fakeOutput.getvalue().strip(), '1')

    def test_pop_front_command(self):
        self.command_handler.handle_command('push_back 1')
        self.command_handler.handle_command('push_back 2')
        self.command_handler.handle_command('push_back 3')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_front')
            self.assertEqual(fakeOutput.getvalue().strip(), '1')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_front')
            self.assertEqual(fakeOutput.getvalue().strip(), '2')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_front')
            self.assertEqual(fakeOutput.getvalue().strip(), '3')

    def test_error_msg_when_push_in_full_deque(self):
        self.command_handler.handle_command('push_back 1')
        self.command_handler.handle_command('push_back 2')
        self.command_handler.handle_command('push_back 3')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('push_back 4')
            self.assertEqual(fakeOutput.getvalue().strip(), 'error')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('push_front 4')
            self.assertEqual(fakeOutput.getvalue().strip(), 'error')

    def test_error_msg_when_pop_from_empty_deque(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_back')
            self.assertEqual(fakeOutput.getvalue().strip(), 'error')

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.command_handler.handle_command('pop_front')
            self.assertEqual(fakeOutput.getvalue().strip(), 'error')


if __name__ == '__main__':
    unittest.main()
