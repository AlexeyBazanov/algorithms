import sys


def main():
    sequence_len = int(sys.stdin.readline().strip())
    sequence = sys.stdin.readline().strip().split()
    distances = [-1] * sequence_len
    
    last_zero_position = None
    
    for i in range(sequence_len):
        if sequence[i] == '0':
            distances[i] = 0
            last_zero_position = i
        else:
            if last_zero_position is None: 
                continue
            else:
                distance = abs((i + 1) - (last_zero_position + 1))

                if distances[i] == -1:
                    distances[i] = distance
                if distance < distances[i]:
                    distances[i] = distance

    for i in range(sequence_len - 1, -1, -1):
        if sequence[i] == '0':
            distances[i] = 0
            last_zero_position = i
        else:
            if last_zero_position is None:
                continue
            else:
                distance = abs((i + 1) - (last_zero_position + 1))

                if distances[i] == -1:
                    distances[i] = distance
                if distance < distances[i]:
                    distances[i] = distance

    print(' '.join(map(str, distances)))


main()
