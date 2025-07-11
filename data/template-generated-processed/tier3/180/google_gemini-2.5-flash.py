def solve():
    """Index: 180.
    Returns: the amount of money Derek has left.
    """
    # L1
    total_money = 960 # Derek has $960
    textbook_divisor = 2 # half of that
    spent_on_textbooks = total_money / textbook_divisor

    # This intermediate calculation is derived from previous steps and used in L2.
    money_left_after_textbooks = total_money - spent_on_textbooks

    # L2
    school_supplies_divisor = 4 # a quarter of what is left
    spent_on_school_supplies = money_left_after_textbooks / school_supplies_divisor

    # L3
    money_left = total_money - spent_on_textbooks - spent_on_school_supplies

    # FA
    answer = money_left
    return answer