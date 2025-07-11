def solve():
    """Index: 1186.
    Returns: the total cost of the ramp installation.
    """
    # L1
    days_worked = 3 # 3 days
    hours_per_day = 5 # 5 hours per day
    contractor_hours = days_worked * hours_per_day

    # L2
    hourly_rate = 150 # $150 an hour
    contractor_cost = hourly_rate * contractor_hours

    # L3
    inspector_discount_percent = 0.8 # 80% less
    inspector_discount_amount = contractor_cost * inspector_discount_percent

    # L4
    inspector_cost = contractor_cost - inspector_discount_amount

    # L5
    permit_cost = 250 # permits which cost $250
    total_cost = permit_cost + inspector_cost + contractor_cost

    # FA
    answer = total_cost
    return answer