def solve():
    """Index: 3663.
    Returns: the total money Beth and Jan have altogether.
    """
    # L1
    beth_would_have = 105 # $105
    beth_more = 35 # $35 more
    beth_money = beth_would_have - beth_more

    # L2
    jan_less = 10 # $10 less
    jan_money = beth_money + jan_less

    # L3
    total_money = beth_money + jan_money

    # FA
    answer = total_money
    return answer