#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        dic1 = {key: value}
        a_dictionary.update(dic1)
        return(a_dictionary)
    else:
        return None
