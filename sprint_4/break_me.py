import polynomial_hash
import random
import string


def brut_force():
    char_set = string.ascii_lowercase

    for i in range(100000000):
        str1 = ''.join(random.sample(char_set*6, random.randint(19, 21)))
        str2 = ''.join(random.sample(char_set*6, random.randint(19, 21)))

        h1 = polynomial_hash.get_hash(str1, 1000, 123987123)
        h2 = polynomial_hash.get_hash(str2, 1000, 123987123)

        if h1 == h2:
            print(str1)
            print(str2)


brut_force()
