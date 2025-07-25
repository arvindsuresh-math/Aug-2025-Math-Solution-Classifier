def solve():
    """Index: 3240.
    Returns: the difference in spending between jewelry and the sweater.
    """
    # L1
    sweater_cost = 40 # spent $40 which is 1/4 of her money on a sweater
    fraction_denominator = 4 # 1/4 of her money
    original_money = sweater_cost * fraction_denominator

    # L2
    money_left_after_sweater = original_money - sweater_cost

    # L3
    money_left_final = 20 # left with $20
    jewelry_cost = money_left_after_sweater - money_left_final

    # L4
    difference_in_spending = jewelry_cost - sweater_cost

    # FA
    answer = difference_in_spending
    return answer