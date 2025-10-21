def find(search_list, value):
    length = len(search_list)
    pointer_lower = 0
    pointer_medium = int(length/2)
    pointer_upper = length - 1
    while pointer_lower <= pointer_upper:
        if value < search_list[pointer_medium]:
            pointer_upper = pointer_medium - 1
            pointer_medium = (pointer_lower + pointer_upper) // 2
        elif value > search_list[pointer_medium]:
            pointer_lower = pointer_medium + 1
            pointer_medium = (pointer_lower + pointer_upper) // 2
        elif value == search_list[pointer_medium]:
            return pointer_medium
    raise ValueError("value not in array")