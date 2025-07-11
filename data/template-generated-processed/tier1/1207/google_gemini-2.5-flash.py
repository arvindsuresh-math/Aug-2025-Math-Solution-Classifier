def solve():
    """Index: 1207.
    Returns: the total number of seashells Nala has.
    """
    # L1
    first_day_seashells = 5 # found 5 seashells
    second_day_seashells = 7 # found another 7
    seashells_first_two_days = first_day_seashells + second_day_seashells

    # L2
    multiplier_third_day = 2 # twice the number she got from the first two days
    seashells_third_day = seashells_first_two_days * multiplier_third_day

    # L3
    total_seashells = seashells_first_two_days + seashells_third_day

    # FA
    answer = total_seashells
    return answer