def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming_distance = 0
    for i, k in enumerate(strand_a):
        if strand_b[i] != k:
            hamming_distance += 1
    return hamming_distance