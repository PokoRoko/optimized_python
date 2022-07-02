from loguru import logger
from scripts import def_time
from mock_data import dict1_5000, dict2_5000


@def_time
def concatinate_dict():
    res = dict1_5000
    for key, value in dict2_5000.items():
        res[key] = value


@def_time
def generate_dict():
    res = {name: operator for name, operator in (dict1_5000.items() | dict2_5000.items())}

@def_time
def generate2_dict():
    res = {**dict1_5000.items,**dict2_5000}

@def_time
def generate3_dict():
    dict(dict1_5000.items() | dict2_5000.items())

@def_time
def generate4_dict():
    res = dict1_5000.copy()
    res.update(dict2_5000)

@def_time
def generate5_dict():
    res = dict1_5000 | dict2_5000




if __name__ == "__main__":
    concatinate_dict()
    generate_dict()
    generate2_dict()
    generate3_dict()
    generate4_dict()