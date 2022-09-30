#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        dict = {}
        tmp = {}
        for key, value in a_dictionary.items():
            new = value * 2
            tmp = {key: new}
            dict.update(tmp)
        return(dict)
    return None
