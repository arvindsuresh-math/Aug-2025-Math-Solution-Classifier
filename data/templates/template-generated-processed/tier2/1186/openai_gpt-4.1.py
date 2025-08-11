def solve():
    """Index: 1186.
    Returns: the total cost for installing the ramp, including permits, contractor, and inspector.
    """
    # L1
    contractor_days = 3 # works for 3 days
    contractor_hours_per_day = 5 # 5 hours per day
    contractor_total_hours = contractor_days * contractor_hours_per_day

    # L2
    contractor_hourly_rate = 150 # $150 an hour
    contractor_total_cost = contractor_hourly_rate * contractor_total_hours

    # L3
    inspector_discount_percent = 0.8 # 80% less
    inspector_discount_amount = contractor_total_cost * inspector_discount_percent

    # L4
    inspector_cost = contractor_total_cost - inspector_discount_amount

    # L5
    permit_cost = 250 # permits cost $250
    total_cost = permit_cost + inspector_cost + contractor_total_cost

    # FA
    answer = total_cost
    return answer