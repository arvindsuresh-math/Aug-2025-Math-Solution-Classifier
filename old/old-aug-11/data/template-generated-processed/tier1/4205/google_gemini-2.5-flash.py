def solve():
    """Index: 4205.
    Returns: the total number of fish-eater birds Cohen saw in three days.
    """
    # L1
    birds_day1 = 300 # 300 fish-eater birds
    doubled_factor = 2 # doubled
    birds_day2 = doubled_factor * birds_day1

    # L2
    total_birds_two_days = birds_day2 + birds_day1

    # L3
    reduced_amount_day3 = 200 # reduced by 200
    birds_day3 = birds_day2 - reduced_amount_day3

    # L4
    total_birds_three_days = birds_day3 + total_birds_two_days

    # FA
    answer = total_birds_three_days
    return answer