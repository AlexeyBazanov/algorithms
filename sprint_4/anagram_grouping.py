import sys

letters_map = {
    'a': 3,
    'b': 5,
    'c': 7,
    'd': 11,
    'e': 13,
    'f': 17,
    'g': 19,
    'h': 23,
    'i': 29,
    'j': 31,
    'k': 37,
    'l': 41,
    'm': 43,
    'n': 47,
    'o': 53,
    'p': 59,
    'q': 61,
    'r': 67,
    's': 71,
    't': 73,
    'u': 79,
    'v': 83,
    'w': 89,
    'x': 97,
    'y': 101,
    'z': 103,
}


def get_str_hash(string):
    h = 1
    for c in string:
        h *= letters_map[c] % 1100101
    return h


def anagram_grouping(strings):
    anagrams = {}

    for i in range(len(strings)):
        str_len = len(strings[i])
        str_hash = get_str_hash(strings[i])

        if str_len not in anagrams:
            anagrams[str_len] = {}

        if str_hash not in anagrams[str_len]:
            anagrams[str_len][str_hash] = []

        anagrams[str_len][str_hash].append(i)

    return anagrams


def sort_anagrams(anagrams):
    sorted_anagrams = {}

    for i in anagrams:
        for j in anagrams[i]:
            if anagrams[i][j][0] not in sorted_anagrams:
                sorted_anagrams[anagrams[i][j][0]] = []
            sorted_anagrams[anagrams[i][j][0]].append(anagrams[i][j])

    return sorted_anagrams


def print_result(anagrams):
    sorted_anagrams = sort_anagrams(anagrams)

    for i in sorted(sorted_anagrams.keys()):
        for a in sorted_anagrams[i]:
            print(' '.join(map(str, a)))


def main():
    sys.stdin.readline()
    strings = sys.stdin.readline().strip().split(' ')
    anagrams = anagram_grouping(strings)
    print_result(anagrams)


if __name__ == '__main__':
    main()
