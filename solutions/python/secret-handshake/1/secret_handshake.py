def commands(binary_str):
    binary = 0
    for i, k in enumerate(binary_str[::-1]):
        if k == "1":
            binary += 2**i
    values = ["wink", "double blink", "close your eyes", "jump"]
    return_list = []
    for i, k in enumerate(values):
        if 2**i & binary:
            return_list.append(k)
    if binary & 16:
        return_list = return_list[::-1]
    return return_list