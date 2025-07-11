def solve():
    """Index: 1528.
    Returns: the amount of money Gabby still needs to buy the makeup set.
    """
    # L1
    set_cost = 65 # The makeup set costs $65
    gabby_has = 35 # she already has $35
    remaining_after_savings = set_cost - gabby_has

    # L2
    mom_gave = 20 # Gabby’s mom gives her an additional $20
    money_needed = remaining_after_savings - mom_gave

    # FA
    answer = money_needed
    return answer