def solve():
    """Index: 915.
    Returns: Allyn's total monthly expenses on electricity in June.
    """
    # L1
    watts_per_bulb_per_day = 60 # uses 60 watts of power each day
    num_bulbs = 40 # has 40 such bulbs
    total_watts_per_day = watts_per_bulb_per_day * num_bulbs

    # L2
    days_in_june = 30 # WK
    total_watts_in_june = days_in_june * total_watts_per_day

    # L3
    cost_per_watt_cents = 0.20 # twenty cents per power watt used
    total_monthly_expenses = total_watts_in_june * cost_per_watt_cents

    # FA
    answer = total_monthly_expenses
    return answer