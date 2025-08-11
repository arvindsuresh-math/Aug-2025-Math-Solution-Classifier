def solve():
    """Index: 4770.
    Returns: the amount of money Ed was left with after paying for his stay at the hotel.
    """
    # L1
    cost_per_hour_night = 1.50 # $1.50 per hour every night
    hours_night = 6 # 6 hours last night
    cost_night = cost_per_hour_night * hours_night

    # L2
    cost_per_hour_morning = 2 # $2 per hour every morning
    hours_morning = 4 # 4 hours this morning
    cost_morning = cost_per_hour_morning * hours_morning

    # L3
    total_spent = cost_night + cost_morning

    # L4
    initial_money = 80 # Ed had $80
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer