import sys


class BracketsValidator:

    def is_valid(self, brackets):
        open_brackets = []
        for bracket in brackets:
            if self.is_open(bracket):
                open_brackets.append(bracket)
            else:
                if self.no_open_brackets_left(open_brackets):
                    return False

                last_open_bracket = open_brackets.pop()

                if not self.is_pair(last_open_bracket, bracket):
                    return False

        return self.no_open_brackets_left(open_brackets)

    def no_open_brackets_left(self, open_brackets):
        return len(open_brackets) == 0

    def is_open(self, bracket):
        return bracket == '(' or bracket == '{' or bracket == '['

    def is_pair(self, open_bracket, close_bracket):
        if open_bracket == '(' and close_bracket == ')':
            return True
        if open_bracket == '{' and close_bracket == '}':
            return True
        if open_bracket == '[' and close_bracket == ']':
            return True

        return False


def main():
    bracket_sequence = sys.stdin.readline().strip()
    brackets_validator = BracketsValidator()
    print(brackets_validator.is_valid(bracket_sequence))


if __name__ == '__main__':
    main()
