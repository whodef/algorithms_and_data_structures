import random
import string

print('100000')


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


i = 1
while i <= 100000:
    print(get_random_string(20), random.randint(0, 10 ** 9), random.randint(0, 10 ** 9))
    i = i + 1
