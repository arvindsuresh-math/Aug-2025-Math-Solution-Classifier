def solve():
    """Index: 7279.
    Returns: the total amount of milk produced per week by the cows.
    """
    # L1
    milk_per_cow_per_day = 1000 # 1000 oz of milk per day
    num_cows = 52 # 52 dairy cows
    milk_per_day = milk_per_cow_per_day * num_cows

    # L2
    days_per_week = 7 # WK
    milk_per_week = milk_per_day * days_per_week

    # FA
    answer = milk_per_week
    return answer