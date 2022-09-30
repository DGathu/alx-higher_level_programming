#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total = 0
        freq = 0
        for tup in my_list:
            (weight, occur) = tup
            total += (weight * occur)
            freq += occur
        return (total/freq) if freq > 0 else 0
    else:
        return (0)
