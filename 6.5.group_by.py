from collections import defaultdict


def group_by(f, iterable):
    res = defaultdict(list)
    for i in iterable:
        key = f(i)
        res[key].append(i)
    return dict(res)



# a = group_by(len, ["hi", "bye", "yo", "try", "oooo", "p"])
# print(a)