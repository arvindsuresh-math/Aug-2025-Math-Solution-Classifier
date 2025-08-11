def solve():
    """Index: 2457.
    Returns: the number of days until the bee colony reaches a fourth of its initial number.
    """
    # L1
    initial_bees = 80000 # A colony of bees can contain up to 80000 individuals
    fraction_denominator = 4 # a fourth of its initial number
    target_bees = initial_bees / fraction_denominator

    # L2
    bees_to_die = initial_bees - target_bees

    # L3
    loss_rate_per_day = 1200 # colony starts to lose 1200 bees per day
    days_to_pass = bees_to_die / loss_rate_per_day

    # FA
    answer = days_to_pass
    return answer