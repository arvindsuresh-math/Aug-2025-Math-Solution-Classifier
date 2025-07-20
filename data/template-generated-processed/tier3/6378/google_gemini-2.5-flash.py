def solve():
    """Index: 6378.
    Returns: the amount of money the tooth fairy left per tooth after the first tooth.
    """
    # L1
    total_baby_teeth = 20 # All 20 of Grant’s baby teeth
    dropped_teeth = 1 # one that he dropped
    swallowed_teeth = 1 # another he swallowed accidentally
    teeth_for_fairy = total_baby_teeth - dropped_teeth - swallowed_teeth

    # L2
    first_tooth_not_counted = 1 # after his first tooth
    teeth_after_first = teeth_for_fairy - first_tooth_not_counted

    # L3
    total_money_received = 54 # total of $54 from the tooth fairy
    first_tooth_money = 20 # The tooth fairy left Grant $20 when he lost his first tooth
    money_after_first_tooth = total_money_received - first_tooth_money

    # L4
    money_per_tooth_after_first = money_after_first_tooth / teeth_after_first

    # FA
    answer = money_per_tooth_after_first
    return answer