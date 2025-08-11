def solve():
    """Index: 4605.
    Returns: the total money Jane will make in 2 weeks.
    """
    # L1
    num_chickens = 10 # 10 chickens
    eggs_per_chicken_per_week = 6 # lay 6 eggs each per week
    eggs_per_week = num_chickens * eggs_per_chicken_per_week

    # L2
    eggs_per_dozen = 12 # $2/dozen
    dozens_per_week = eggs_per_week / eggs_per_dozen

    # L3
    price_per_dozen = 2 # $2/dozen
    money_per_week = dozens_per_week * price_per_dozen

    # L4
    num_weeks = 2 # in 2 weeks
    total_money = num_weeks * money_per_week

    # FA
    answer = total_money
    return answer