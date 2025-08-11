def solve():
    """Index: 1506.
    Returns: the number of brownies left after all are eaten and shared.
    """
    # L1
    tina_per_day = 2 # one with lunch and dinner every day
    tina_days = 5 # for 5 days
    tina_ate = tina_per_day * tina_days

    # L2
    husband_per_day = 1 # husband snagged one per day
    husband_days = 5 # for 5 days
    husband_ate = husband_per_day * husband_days

    # L3
    total_brownies = 24 # cut it into 24 pieces
    guests_ate = 4 # shared 4 with dinner guests
    brownies_left = total_brownies - tina_ate - husband_ate - guests_ate

    # FA
    answer = brownies_left
    return answer