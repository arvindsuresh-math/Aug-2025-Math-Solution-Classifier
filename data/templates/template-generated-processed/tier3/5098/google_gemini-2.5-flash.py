def solve():
    """Index: 5098.
    Returns: the number of teslas Elon has.
    """
    # L1
    chris_teslas = 6 # Chris has 6 teslas
    half_divisor = 2 # half the number
    sam_teslas = chris_teslas / half_divisor

    # L2
    more_teslas_for_elon = 10 # Elon has 10 more teslas
    elon_teslas = more_teslas_for_elon + sam_teslas

    # FA
    answer = elon_teslas
    return answer