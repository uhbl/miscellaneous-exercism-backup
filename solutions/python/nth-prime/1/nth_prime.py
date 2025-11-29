def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number == 1:
        return 2
    if number == 2:
        return 3
    counter = 2
    prime = 3
    while number > counter:
        prime += 2
        is_prime = True
        for i in range(1, prime, 2)[1::]:
            if prime % i == 0:
                is_prime = False
        if is_prime:
            counter += 1
    return prime