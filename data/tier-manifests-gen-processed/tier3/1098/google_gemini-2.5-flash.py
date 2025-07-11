def solve():
    """Index: 1098.
    Returns: the number of weeks the watermelons will last.
    """
    # L1
    eats_per_week = 3 # eats 3 watermelons per week
    gives_to_dad_per_week = 2 # gives 2 to his dad
    total_consumed_per_week = eats_per_week + gives_to_dad_per_week

    # L2
    initial_watermelons = 30 # buys 30 watermelons
    weeks_last = initial_watermelons / total_consumed_per_week

    # FA
    answer = weeks_last
    return answer