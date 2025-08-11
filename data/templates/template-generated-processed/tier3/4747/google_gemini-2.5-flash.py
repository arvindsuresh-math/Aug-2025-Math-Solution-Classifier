def solve():
    """Index: 4747.
    Returns: the difference in toothbrushes given out between the busiest and slowest months.
    """
    # L1
    january_giveaway = 53 # 53 toothbrushes in January
    february_giveaway = 67 # 67 toothbrushes in February
    march_giveaway = 46 # 46 toothbrushes in March
    total_given_through_march = january_giveaway + february_giveaway + march_giveaway

    # L2
    initial_toothbrushes = 330 # 330 toothbrushes to give away
    remaining_before_april = initial_toothbrushes - total_given_through_march

    # L3
    months_remaining_division = 2 # half each month
    giveaway_per_month_april_may = remaining_before_april / months_remaining_division

    # L5
    difference_busiest_slowest = giveaway_per_month_april_may - march_giveaway

    # FA
    answer = difference_busiest_slowest
    return answer