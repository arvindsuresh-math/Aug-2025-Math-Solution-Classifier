def solve():
    """Index: 3470.
    Returns: the total cost of the repairs.
    """
    # L1
    labor_hours = 16 # 16 hours
    hourly_rate = 75 # $75 an hour
    labor_cost = labor_hours * hourly_rate

    # L2
    part_cost = 1200 # The part itself cost $1200
    total_cost = labor_cost + part_cost

    # FA
    answer = total_cost
    return answer