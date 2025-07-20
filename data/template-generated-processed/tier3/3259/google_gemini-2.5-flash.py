def solve():
    """Index: 3259.
    Returns: the initial amount of money his brother had.
    """
    # L1
    michael_initial_money = 42 # Michael has $42
    half_divisor = 2 # half the money
    money_michael_gives_away = michael_initial_money / half_divisor

    # L2
    brother_money_left = 35 # his brother has $35 left
    candy_cost = 3 # buys 3 dollars worth of candy
    brother_money_before_candy = brother_money_left + candy_cost

    # L3
    brother_initial_money = brother_money_before_candy - money_michael_gives_away

    # FA
    answer = brother_initial_money
    return answer