import sys


def generate_brackets(n, counter_open, counter_close, sequence):
    if counter_open + counter_close == n * 2:
        print(sequence)
    if counter_open < n:
        generate_brackets(n, counter_open + 1, counter_close, sequence + "(")
    if counter_open > counter_close:
        generate_brackets(n, counter_open, counter_close + 1, sequence + ")")


n = int(sys.stdin.readline().strip())

generate_brackets(n, 0, 0, "")
