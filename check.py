from scripts import def_time
data = (i**2+1 for i in range(100000))

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
    list_a = [2*i-1 for i in range(1000000)]
    list_b = [i**2 for i in list_a]
    _=list_b[list_a.index(876567)]

@def_time
def fast_search_in_dict():
    list_a = [2 * i - 1 for i in range(1000000)]
    list_b = [i ** 2 for i in list_a]
    dict_ab = dict(zip(list_a, list_b))
    _ = list_b[dict_ab.get(876567,None)]


