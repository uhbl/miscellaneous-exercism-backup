def square_root(number):
    d = len(str(number))
    if d % 2 == 0:
        sqrt_digits = d // 2
    else:
        sqrt_digits = (d + 1) // 2
    counter = 0
    start = int("1" + "0" * (sqrt_digits - 1))
    end = int("1" + "0" * (sqrt_digits))
    pointer = 0
    while counter < 100:
        counter += 1
        pointer = (start + end) / 2
        if pointer * pointer > number:
            end = pointer
        elif pointer * pointer < number:
            start = pointer
    return pointer