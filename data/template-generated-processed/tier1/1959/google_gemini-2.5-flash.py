def solve():
    """Index: 1959.
    Returns: the amount of money Abigail has lost.
    """
    # L1
    start_money = 11 # She had $11 in her purse at the start of the day
    spent_money = 2 # she spent $2 in a store
    money_after_shopping_expected = start_money - spent_money

    # L2
    money_left_actual = 3 # she now has $3 left
    money_lost = money_after_shopping_expected - money_left_actual

    # FA
    answer = money_lost
    return answer