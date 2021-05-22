import sys


class BracketSequence:

    def __init__(self, brackets_string):
        self.left_brackets = []
        self.right_brackets = []
        self.collect_brackets(brackets_string)
        self.left_brackets_len = len(self.left_brackets)
        self.right_brackets_len = len(self.right_brackets)

    def is_correct(self):
        if self.left_brackets_len == 0 and self.right_brackets_len == 0:
            print('Is null')
            return True

        if self.left_brackets_len != self.right_brackets_len:
            print('Diff len')
            return False

        self.delete_closest_opposite_brackets()

        return self.is_brackets_sequence_equal()

    def is_brackets_sequence_equal(self):
        right_index = -1

        for left_index in range(self.left_brackets_len):
            if not self.is_opposite_brackets(self.left_brackets[left_index], self.right_brackets[right_index]):
                return False

            right_index -= 1

        return True

    def delete_closest_opposite_brackets(self):
        index = 0
        left_brackets = []
        right_brackets = []

        while index < self.left_brackets_len:
            if not self.is_opposite_brackets(self.left_brackets[index], self.right_brackets[index]):
                left_brackets.append(self.left_brackets[index])
                right_brackets.append(self.left_brackets[index])

            index += 1

        self.left_brackets = left_brackets
        self.right_brackets = right_brackets
        self.left_brackets_len = len(self.left_brackets)
        self.right_brackets_len = len(self.right_brackets)

    def collect_brackets(self, brackets_string):
        for bracket in brackets_string:
            if self.is_left_bracket(bracket):
                self.left_brackets.append(bracket)
            else:
                self.right_brackets.append(bracket)

    def is_left_bracket(self, bracket):
        return bracket == '(' or bracket == '{' or bracket == '['

    def is_opposite_brackets(self, left_bracket, right_bracket):
        if left_bracket == '(' and right_bracket == ')':
            return True
        if left_bracket == '{' and right_bracket == '}':
            return True
        if left_bracket == '[' and right_bracket == ']':
            return True

        return False


def main():
    bracket_sequence_string = sys.stdin.readline().strip()
    bracket_sequence = BracketSequence(bracket_sequence_string)

    print(bracket_sequence.is_correct())


if __name__ == '__main__':
    main()
