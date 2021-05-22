import sys


def is_sub_sequence(needle, haystack):
    letters_found = 0
    last_haystack_index = 0

    if len(haystack) < len(needle):
        return False

    for needle_letter in needle:
        for haystack_index in range(last_haystack_index, len(haystack)):
            last_haystack_index += 1
            if needle_letter == haystack[haystack_index]:
                letters_found += 1
                break

    return letters_found == len(needle)


def main():
    needle = sys.stdin.readline().strip()
    haystack = sys.stdin.readline().strip()
    print(is_sub_sequence(needle, haystack))


main()

