import random
import string


def unique_strings(len_string: int = 5) -> str:
    random_string = ''.join(random.choices(string.ascii_letters, k=len_string))
    return random_string


def generate_dict(len_dict):
    res = {}
    for i in range(len_dict):
        res[unique_strings()] = unique_strings(100)
    return res


print(generate_dict(5000))
