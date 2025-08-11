def solve():
    """Index: 3821.
    Returns: the original amount of money Anna had.
    """
    # L1
    spent_fraction = 1/4 # Anna spent 1/4 of her money
    money_left = 24 # now she has $24 left
    # The line sets up the equation: original_money - original_money * spent_fraction = money_left

    # L2
    remaining_fraction = 1 - spent_fraction # Combining like terms (1 - 1/4 = 3/4)
    # The line simplifies the equation to: original_money * remaining_fraction = money_left

    # L3
    original_money = money_left / remaining_fraction # Dividing both sides by remaining_fraction

    # FA
    answer = original_money
    return answer