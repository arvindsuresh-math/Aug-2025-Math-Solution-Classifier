def solve():
    """Index: 4888.
    Returns: the amount of money Patrick has now.
    """
    # L1
    bicycle_price = 150 # bicycle that costs $150
    half_divisor = 2 # WK
    saved_money = bicycle_price / half_divisor

    # L2
    lent_money = 50 # lent $50 to his friend
    money_now = saved_money - lent_money

    # FA
    answer = money_now
    return answer