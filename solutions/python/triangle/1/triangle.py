def is_triangle(sides):
    sums_list = [sides[1] + sides[2], sides[0] + sides[2], sides[0] + sides[1]]
    for i, k in enumerate(sides):
        if k < 0 or k == 0:
            return False
        if k > sums_list[i]:
            return False
    return True

def equilateral(sides):
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    else:
        return False 


def isosceles(sides):
    if not is_triangle(sides):
        return False
    sums_pair = [sides[i] == sides[(i + 1) % len(sides)] for i, k in enumerate(sides)]
    for i in sums_pair:
        if i is True:
            return True
    return False
    


def scalene(sides):
    if not is_triangle(sides):
        return False
    sums_pair = [sides[i] == sides[(i + 1) % len(sides)] for i, k in enumerate(sides)]
    counter = 0
    for i in sums_pair:
        if i is True:
            counter += 1
    if counter == 0:
        return True
    return False