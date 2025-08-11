def solve():
    """Index: 6728.
    Returns: the total money his brother had in the end.
    """
    # L1
    michael_initial_money = 42 # Michael has $42
    money_given_divisor = 2 # gives away half the money
    money_michael_gives_away = michael_initial_money / money_given_divisor

    # L2
    brother_initial_money = 17 # His brother has $17
    brother_money_after_receiving = money_michael_gives_away + brother_initial_money

    # L3
    candy_cost = 3 # buys 3 dollars worth of candy
    brother_final_money = brother_money_after_receiving - candy_cost

    # FA
    answer = brother_final_money
    return answer