import sys


def get_hash(string, base, mod):
    h = 0
    for c in string:
        h = (h * base + ord(c)) % mod
    return h


if __name__ == '__main__':
    base = int(sys.stdin.readline().strip())
    mod = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()
    print(get_hash(string, base, mod))



