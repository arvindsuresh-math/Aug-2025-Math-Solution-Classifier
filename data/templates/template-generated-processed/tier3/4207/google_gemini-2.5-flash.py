def solve():
    """Index: 4207.
    Returns: the amount of money left in Mitzel's allowance.
    """
    # L1
    spent_percentage = 35 # 35% of her allowance
    total_percentage = 100 # WK
    remaining_percentage = total_percentage - spent_percentage

    # L2
    spent_amount = 14 # If she spent $14
    amount_left = remaining_percentage * spent_amount / spent_percentage

    # FA
    answer = amount_left
    return answer