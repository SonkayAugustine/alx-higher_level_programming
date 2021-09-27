#!/usr/bin/python3
def best_score(a_dictionary):
    b_score = 0
    key = ''
    if a_dictionary is None:
        return None
    else:
        for k, v in a_dictionary.items():
            if v > b_score:
                b_score = v
                key = k
    if b_score == 0:
        return None
    return key
