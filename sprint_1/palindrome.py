import sys


def is_palindrome(string):
    string_length = len(string)
    string_middle = int(round(string_length / 2))

    left_symbol_pos = 0
    right_symbol_pos = -1

    for i in range(string_middle):
        while left_symbol_pos < string_length and not string[left_symbol_pos].isalnum():
            left_symbol_pos += 1

        while abs(right_symbol_pos) < string_length and not string[right_symbol_pos].isalnum():
            right_symbol_pos -= 1

        if string[left_symbol_pos].lower() != string[right_symbol_pos].lower():
            return False

        left_symbol_pos += 1
        right_symbol_pos -= 1

    return True


def main():
    string = sys.stdin.readline().strip()
    print('True' if is_palindrome(string) else 'False')


main()



