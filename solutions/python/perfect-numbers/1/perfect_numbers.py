def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    upper_bound = int(number ** (1/2)) + 1
    factors = [1]
    for i in range(2, upper_bound):
        if number % i == 0:
            if i != (number / i):
                factors.append(i)
                factors.append(int(number / i))
            else:
                factors.append(i)
    aliquot_sum = sum(factors)
    if aliquot_sum < number:
        return "deficient"
    elif aliquot_sum == number:
        return "perfect"
    else:
        return "abundant"