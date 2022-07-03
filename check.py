from scripts import def_time

data = (i ** 2 + 1 for i in range(100000))


@def_time
def search_in_list(data):
    list_data = list(data)
    _ = 1098987 in list_data


@def_time
def search_in_set(data):
    set_data = set(data)
    _ = 1098987 in set_data


@def_time
# используйте dict вместо двух списков для поиска соответствия
def low_search_in_two_list():
    list_a = [2 * i - 1 for i in range(1000000)]
    list_b = [i ** 2 for i in list_a]
    _ = list_b[list_a.index(876567)]


@def_time
def fast_search_in_dict():
    list_a = [2 * i - 1 for i in range(1000000)]
    list_b = [i ** 2 for i in list_a]
    dict_ab = dict(zip(list_a, list_b))
    _ = list_b[dict_ab.get(876567, None)]


# предпочитайте использовать цикл for вместо цикла while
@def_time
def low_while_or_for():
    s, i = 0, 0
    while i < 10000:
        i = + 1
        s = s + 1
    print(s)


@def_time
def fast_while_or_for():
    s = 0
    for i in range(1, 10001):
        s = s + 1
    print(s)


# избегайте двойного вычисления в теле цикла
@def_time
def low_def_in_generator():
    a = [i ** 2 + 1 for i in range(2000)]
    b = [i / sum(a) for i in a]


@def_time
def fast_def_in_generator():
    a = [i ** 2 + 1 for i in range(2000)]
    sum_a = sum(a)
    b = [i / sum_a for i in a]


# замените рекурсивную функцию на механизм цикла
def low_fib(n=30):
    res = (1 if n in (1, 2) else low_fib(n - 1) + low_fib(n - 2))


def fast_fib(n=30):
    if n in (1, 2):
        return (1)
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b
