def solve():
    """Index: 1116.
    Returns: the number of days that have elapsed.
    """
    # L2
    start_amount = 50 # starts each day with $50
    spend_per_day = 15 # spends $15 every day
    save_per_day = start_amount - spend_per_day

    # L3
    # Let the number of days be x (unknown)
    # L4
    mom_multiplier = 2 # mom doubled his total savings
    after_mom = save_per_day * mom_multiplier

    # L5
    dad_add = 10 # dad gave him an additional $10
    final_amount = 500 # he now has $500
    # after_mom * x + dad_add = final_amount
    # L6
    after_mom_total = final_amount - dad_add

    # L7
    x = after_mom_total // after_mom

    # FA
    answer = x
    return answer