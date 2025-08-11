def solve():
    """Index: 1457.
    Returns: the total number of sacks of rice after the first and second harvest.
    """
    # L1
    initial_yield = 20 # 20 sacks of rice
    yield_increase_percent = 0.20 # twenty percent
    increase_first_harvest = initial_yield * yield_increase_percent

    # L2
    yield_second_harvest = initial_yield + increase_first_harvest

    # L3
    total_sacks = initial_yield + yield_second_harvest

    # FA
    answer = total_sacks
    return answer