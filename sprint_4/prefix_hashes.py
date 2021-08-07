import sys

hash_map = []


def get_hash_with_offset(string, prev_hash, base, mod):
    return (prev_hash * base + ord(string[len(string)-1])) % mod


def save_hash_map(string, base, mod):
    offset = 0
    while offset < len(string):
        hash_map.append([])
        map_index = 0

        for i in range(offset, len(string)):
            if map_index == 0:
                hash_map[offset].append(ord(string[offset:i+1]) % mod)
                map_index += 1
            else:
                hash_map[offset].append(get_hash_with_offset(string[offset:i+1], hash_map[offset][map_index-1], base, mod))
                map_index += 1

        offset += 1


def get_substring_hash(left, right):
    return hash_map[left-1][right-left]


def main():
    base = int(sys.stdin.readline().strip())
    mod = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()
    commands = int(sys.stdin.readline().strip())
    result = ''

    save_hash_map(string, base, mod)

    for i in range(commands):
        interval = sys.stdin.readline().strip().split(' ')
        left = int(interval[0])
        right = int(interval[1])
        result = result + str(get_substring_hash(left, right)) + "\n"

    print(result.strip())


if __name__ == '__main__':
    main()
