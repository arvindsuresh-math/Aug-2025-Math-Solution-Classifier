def solve():
    """Index: 3827.
    Returns: the amount of money Jericho will be left with after paying his debts.
    """
    # L1
    total_twice_money = 60 # Twice the money Jericho has is 60
    divisor_for_jericho_money = 2 # Twice the money Jericho has
    jericho_money = total_twice_money / divisor_for_jericho_money

    # L2
    annika_debt = 14 # He owes Annika $14
    manny_debt_divisor = 2 # owes half as much to Manny
    manny_debt = annika_debt / manny_debt_divisor

    # L3
    total_debts = annika_debt + manny_debt

    # L4
    money_left = jericho_money - total_debts

    # FA
    answer = money_left
    return answer