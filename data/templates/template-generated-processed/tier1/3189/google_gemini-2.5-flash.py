def solve():
    """Index: 3189.
    Returns: the total number of eggs Gary collects per week.
    """
    # L1
    initial_chickens = 4 # Gary buys 4 chickens
    multiplier_after_two_years = 8 # 8 times as many chickens
    chickens_after_two_years = initial_chickens * multiplier_after_two_years

    # L2
    eggs_per_chicken_per_day = 6 # each chicken lays 6 eggs a day
    eggs_per_day = chickens_after_two_years * eggs_per_chicken_per_day

    # L3
    days_per_week = 7 # WK
    eggs_per_week = eggs_per_day * days_per_week

    # FA
    answer = eggs_per_week
    return answer