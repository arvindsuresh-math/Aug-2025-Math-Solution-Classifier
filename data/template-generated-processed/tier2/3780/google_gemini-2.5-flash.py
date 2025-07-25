def solve():
    """Index: 3780.
    Returns: the total number of birds Janet counts.
    """
    # L1
    hawks_percentage_increase_num = 60 # 60% more hawks
    crows_count = 30 # 30 crows
    percent_factor = 0.01 # WK
    more_hawks_than_crows = hawks_percentage_increase_num * percent_factor * crows_count

    # L2
    total_hawks = more_hawks_than_crows + crows_count

    # L3
    total_birds = total_hawks + crows_count

    # FA
    answer = total_birds
    return answer