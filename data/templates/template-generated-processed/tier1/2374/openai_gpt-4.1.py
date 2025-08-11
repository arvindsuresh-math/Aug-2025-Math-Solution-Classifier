def solve():
    """Index: 2374.
    Returns: the total cost to employ all employees for one 8-hour shift.
    """
    # L1
    num_employees_12 = 200 # 200 of them earn $12 per hour
    wage_12 = 12 # $12 per hour
    cost_12_per_hour = num_employees_12 * wage_12

    # L2
    num_employees_14 = 40 # 40 of them earn $14 per hour
    wage_14 = 14 # $14 per hour
    cost_14_per_hour = num_employees_14 * wage_14

    # L3
    total_employees = 300 # there are 300 employees
    num_employees_17 = total_employees - num_employees_12 - num_employees_14

    # L4
    wage_17 = 17 # $17 per hour
    cost_17_per_hour = num_employees_17 * wage_17

    # L5
    total_cost_per_hour = cost_12_per_hour + cost_14_per_hour + cost_17_per_hour

    # L6
    shift_hours = 8 # one 8-hour long shift
    total_shift_cost = shift_hours * total_cost_per_hour

    # FA
    answer = total_shift_cost
    return answer