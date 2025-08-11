def solve():
    """Index: 1764.
    Returns: the number of fish by which the fisherman with the higher catch exceeds the other at the end of the season.
    """
    # L1
    first_fisherman_rate = 3 # catch fish at a steady rate of 3 per day
    season_days = 213 # lasting exactly 7 months, or 213 days
    first_fisherman_total = first_fisherman_rate * season_days

    # L2
    second_fisherman_rate1 = 1 # 1 fish per day during the first 30 days
    days1 = 30 # first 30 days
    second_fisherman_rate2 = 2 # 2 fish per day during the next 60 days
    days2 = 60 # next 60 days
    second_fisherman_first_90 = second_fisherman_rate1 * days1 + second_fisherman_rate2 * days2

    # L3
    days_first_two_periods = days1 + days2
    remaining_days = season_days - days_first_two_periods
    second_fisherman_rate3 = 4 # 4 fish per day during the remainder
    second_fisherman_remaining = second_fisherman_rate3 * remaining_days

    # L4
    second_fisherman_total = second_fisherman_first_90 + second_fisherman_remaining

    # L5
    difference = second_fisherman_total - first_fisherman_total

    # FA
    answer = difference
    return answer