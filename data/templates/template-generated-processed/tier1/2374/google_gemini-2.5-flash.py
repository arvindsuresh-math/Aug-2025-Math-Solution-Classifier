def solve():
    """Index: 2374.
    Returns: the total cost to employ all people for one 8-hour long shift.
    """
    # L1
    employees_group1 = 200 # 200 of them
    hourly_rate_group1 = 12 # $12 per hour
    cost_group1_per_hour = employees_group1 * hourly_rate_group1

    # L2
    employees_group2 = 40 # 40 of them
    hourly_rate_group2 = 14 # $14 per hour
    cost_group2_per_hour = employees_group2 * hourly_rate_group2

    # L3
    total_employees = 300 # 300 employees
    employees_group3 = total_employees - employees_group1 - employees_group2

    # L4
    hourly_rate_group3 = 17 # $17 per hour
    cost_group3_per_hour = employees_group3 * hourly_rate_group3

    # L5
    total_cost_per_hour = cost_group1_per_hour + cost_group2_per_hour + cost_group3_per_hour

    # L6
    shift_hours = 8 # one 8-hour long shift
    total_cost_per_shift = shift_hours * total_cost_per_hour

    # FA
    answer = total_cost_per_shift
    return answer