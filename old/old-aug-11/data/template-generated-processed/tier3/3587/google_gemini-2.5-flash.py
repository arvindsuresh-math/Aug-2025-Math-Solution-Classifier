def solve():
    """Index: 3587.
    Returns: the number of dancer students who did not slow dance.
    """
    # L1
    total_kids_prom = 140 # 140 kids in the junior prom
    fraction_denominator = 4 # a fourth of them
    dancers = total_kids_prom / fraction_denominator

    # L2
    slow_dancers = 25 # 25 danced the slow dance
    non_slow_dancers = dancers - slow_dancers

    # FA
    answer = non_slow_dancers
    return answer