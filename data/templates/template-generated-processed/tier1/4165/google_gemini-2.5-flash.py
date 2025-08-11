def solve():
    """Index: 4165.
    Returns: the total number of sandwiches Paul would eat if he studied 6 days in a row.
    """
    # L1
    sandwiches_day1 = 2 # eats 2 sandwiches the first day
    multiplier_double = 2 # doubles that number of sandwiches
    sandwiches_day2 = sandwiches_day1 * multiplier_double

    # L2
    sandwiches_day3 = sandwiches_day2 * multiplier_double

    # L3
    total_sandwiches_3_days = sandwiches_day1 + sandwiches_day2 + sandwiches_day3

    # L4
    total_study_days = 6 # studied 6 days in a row
    days_per_cycle = 3 # every three days
    num_cycles = total_study_days / days_per_cycle
    total_sandwiches_6_days = total_sandwiches_3_days * num_cycles

    # FA
    answer = total_sandwiches_6_days
    return answer