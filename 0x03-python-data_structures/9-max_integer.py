#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        biggy = my_list[0]
        for i in my_list:
            if i > biggy:
                biggy = i
        return biggy
    else:
        return None
