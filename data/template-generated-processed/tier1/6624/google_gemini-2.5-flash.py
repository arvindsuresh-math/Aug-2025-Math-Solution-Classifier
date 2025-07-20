def solve():
    """Index: 6624.
    Returns: the amount of money Mia has.
    """
    # L1
    multiplier_for_twice = 2 # twice as much money
    darwin_money = 45 # Darwin has $45
    twice_darwin_money = multiplier_for_twice * darwin_money

    # L2
    mia_more_than_twice = 20 # $20 more than twice as much money
    mia_money = mia_more_than_twice + twice_darwin_money

    # FA
    answer = mia_money
    return answer