def solve():
    """Index: 2846.
    Returns: the amount of money Chris will have left over after his purchases.
    """
    # L1
    game_cost = 60 # video game that costs $60
    candy_cost = 5 # candy that costs $5
    total_spent = game_cost + candy_cost

    # L2
    babysitting_rate = 8 # $8 per hour
    babysitting_hours = 9 # works 9 hours
    total_earned = babysitting_rate * babysitting_hours

    # L3
    money_left = total_earned - total_spent

    # FA
    answer = money_left
    return answer