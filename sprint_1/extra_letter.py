import sys


def extra_letter(original_str, shuffle_str):
    original_str_letters_counter = dict()
    shuffle_str_letters_counter = dict()
    original_str_len = len(original_str)

    for i in range(original_str_len):
        if original_str[i] in original_str_letters_counter:
            original_str_letters_counter[original_str[i]] += 1
        else:
            original_str_letters_counter[original_str[i]] = 1

        if shuffle_str[i] in shuffle_str_letters_counter:
            shuffle_str_letters_counter[shuffle_str[i]] += 1
        else:
            shuffle_str_letters_counter[shuffle_str[i]] = 1

    if shuffle_str[original_str_len] in shuffle_str_letters_counter:
        shuffle_str_letters_counter[shuffle_str[original_str_len]] += 1
    else:
        shuffle_str_letters_counter[shuffle_str[original_str_len]] = 1

    for letter in shuffle_str_letters_counter:
        if letter not in original_str_letters_counter:
            return letter
        if original_str_letters_counter[letter] != shuffle_str_letters_counter[letter]:
            return letter

    return ''


def main():
    original_str = sys.stdin.readline().strip()
    shuffle_str = sys.stdin.readline().strip()
    print(extra_letter(original_str, shuffle_str))


main()
