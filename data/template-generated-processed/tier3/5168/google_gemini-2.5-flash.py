def solve():
    """Index: 5168.
    Returns: the amount of money left over in dollars.
    """
    # L1
    initial_money = 204 # $204 in her piggy bank
    spent_fraction_denominator_toy = 2 # spent half the amount
    money_after_toy = initial_money / spent_fraction_denominator_toy

    # L2
    spent_fraction_denominator_book = 2 # spent half of the remaining money
    money_left_over = money_after_toy / spent_fraction_denominator_book

    # FA
    answer = money_left_over
    return answer