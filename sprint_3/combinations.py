import sys


def get_words(numbers):
    dictionary = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    acceptable_numbers = '23456789'
    words = []

    for number in numbers:
        if number in acceptable_numbers:
            words.append(dictionary[number])

    return words


def get_combinations_count(words):
    count = 1

    for word in words:
        count *= len(word)

    return count


def print_combinations(words, word_index, sequence, combinations, combinations_count):
    if word_index == len(words):
        combinations_count -= 1
        print(sequence, end=" " if combinations_count > 0 else "\n")
        return combinations_count

    for letter in words[word_index]:
        combinations_count = print_combinations(words, word_index + 1, sequence + letter, combinations, combinations_count)

    return combinations_count


def main():
    numbers = sys.stdin.readline().strip()
    words = get_words(numbers)
    combinations_count = get_combinations_count(words)
    print_combinations(words, 0, '', '', combinations_count)


if __name__ == '__main__':
    main()
