def solve():
    """Index: 5284.
    Returns: the total money Kelly will make from selling eggs.
    """
    # L1
    days_per_week = 7 # WK
    eggs_per_chicken_per_day = 3 # lay 3 eggs each per day
    eggs_per_chicken_per_week = days_per_week * eggs_per_chicken_per_day

    # L2
    num_chickens = 8 # 8 chickens
    total_eggs_per_week = eggs_per_chicken_per_week * num_chickens

    # L3
    num_weeks = 4 # in 4 weeks
    total_eggs_in_4_weeks = total_eggs_per_week * num_weeks

    # L4
    eggs_per_dozen = 12 # WK
    total_dozens = total_eggs_in_4_weeks / eggs_per_dozen

    # L5
    price_per_dozen = 5 # $5 a dozen
    total_money_made = total_dozens * price_per_dozen

    # FA
    answer = total_money_made
    return answer