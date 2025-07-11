def solve():
    """Index: 1207.
    Returns: the total number of seashells Nala has.
    """
    # L1
    first_day = 5 # Nala found 5 seashells at the beach
    second_day = 7 # she found another 7
    first_two_days = first_day + second_day

    # L2
    multiplier_third_day = 2 # twice the number she got from the first two days
    third_day = first_two_days * multiplier_third_day

    # L3
    total_seashells = first_two_days + third_day

    # FA
    answer = total_seashells
    return answer