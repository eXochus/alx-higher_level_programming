#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == 0:
        return None
    maxval = 0
    maxkey = None
    for k, v in a_dictionary.items():
        if v > maxval:
            maxval = v
            maxval = k
    return maxkey
