def solve():
    """Index: 2846.
    Returns: the amount of money left over after purchases.
    """
    # L1
    game_cost = 60 # video game that costs $60
    candy_cost = 5 # assortment of candy that costs $5
    total_cost = game_cost + candy_cost

    # L2
    hourly_rate = 8 # $8 per hour
    hours_worked = 9 # works 9 hours
    total_earnings = hourly_rate * hours_worked

    # L3
    money_left_over = total_earnings - total_cost

    # FA
    answer = money_left_over
    return answer