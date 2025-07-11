def solve():
    """Index: 2904.
    Returns: the number of hours the mechanic worked.
    """
    # L1
    labor_cost_per_minute = 0.5 # labor cost .5 dollars a minute
    minutes_per_hour = 60 # WK
    labor_cost_per_hour = labor_cost_per_minute * minutes_per_hour

    # L2
    cost_per_part = 20 # two parts that cost 20 dollars each
    num_parts = 2 # two parts
    total_parts_cost = cost_per_part * num_parts

    # L3
    total_spent = 220 # Mark spent 220 dollars
    total_labor_cost = total_spent - total_parts_cost

    # L4
    hours_worked = total_labor_cost / labor_cost_per_hour

    # FA
    answer = hours_worked
    return answer