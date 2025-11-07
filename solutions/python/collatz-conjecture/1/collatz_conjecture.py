def steps(number):
    total_steps = 0
    number = number
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            total_steps += 1
        else:
            number = 3 * number + 1
            total_steps += 1
    return total_steps