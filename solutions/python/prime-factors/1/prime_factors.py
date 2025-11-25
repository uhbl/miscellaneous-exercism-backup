def factors(value):
    biggest_factor = value
    initial_prime = 2
    prime_factors = []
    while biggest_factor >= initial_prime:
        if biggest_factor % initial_prime == 0:
            biggest_factor = biggest_factor / initial_prime
            prime_factors.append(initial_prime)
        else:
            initial_prime += 1
    return prime_factors