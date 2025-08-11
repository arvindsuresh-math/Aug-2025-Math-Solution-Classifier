def solve():
    """Index: 174.
    Returns: the total amount Glenn spends on movie tickets on Wednesday and Saturday.
    """
    # L1
    monday_price = 5 # Movie tickets cost $5 each on a Monday
    wednesday_multiplier = 2 # twice as much on a Wednesday
    wednesday_price = monday_price * wednesday_multiplier

    # L2
    saturday_multiplier = 5 # five times as much as Monday on a Saturday
    saturday_price = monday_price * saturday_multiplier

    # L3
    total_spent = wednesday_price + saturday_price

    # FA
    answer = total_spent
    return answer