def solve():
    """Index: 3874.
    Returns: the total money collected by Sara.
    """
    # L1
    days_per_week = 5 # five weekdays
    cakes_per_day = 4 # makes 4 cakes a day
    cakes_per_week = days_per_week * cakes_per_day

    # L2
    price_per_cake = 8 # sells her cakes for $8
    money_per_week = cakes_per_week * price_per_cake

    # L3
    num_weeks = 4 # In 4 weeks
    total_money_collected = money_per_week * num_weeks

    # FA
    answer = total_money_collected
    return answer