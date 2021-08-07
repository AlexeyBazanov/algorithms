import sys


def get_pref_hashes(string, base, mod):
    h = [0]
    for i in range(0, len(string)):
        a = h[i] % mod
        b = base % mod
        c = ord(string[i])
        h.append((a * b + c) % mod)
    return h


def get_substring_hash(l, r, mod, base, h):
    a = h[r + 1]
    b = ((h[l] % mod) * pow(base, (r - l + 1), mod)) % mod
    return (a % mod - b % mod) % mod


def main():
    base = int(sys.stdin.readline().strip())
    mod = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()
    commands = int(sys.stdin.readline().strip())

    h = get_pref_hashes(string, base, mod)

    for i in range(commands):
        interval = sys.stdin.readline().strip().split(' ')
        left = int(interval[0])
        right = int(interval[1])

        if left == 1:
            print(h[right])
        else:
            print(get_substring_hash(left-1, right-1, mod, base, h))


if __name__ == '__main__':
    main()
