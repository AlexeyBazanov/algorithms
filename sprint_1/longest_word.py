import sys


def main():
    string_len = int(sys.stdin.readline().strip()) + 1
    string = sys.stdin.readline().rstrip('\n') + ' '
    longest_word_len = 0
    longest_word = ''
    current_word_len = 0
    current_word = ''

    for i in range(string_len):
        if string[i] == ' ':
            if current_word_len > longest_word_len:
                longest_word_len = current_word_len
                longest_word = current_word
            current_word_len = 0
            current_word = ''
        else:
            current_word_len += 1
            current_word += string[i]

    print(longest_word)
    print(longest_word_len)


main()
