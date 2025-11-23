
def flatten(iterable):
    result = []
    for i in iterable:
        if isinstance(i, list):
            result.extend(flatten(i))
        elif i is not None:
            result.append(i)
    return result

"""
def recurse(nest):
    for i in nest:
        if type(i) == type([]):
            recurse(i)
        elif i == None:
            continue
        else:
            flattened.append(i)
"""