def solve():
    """Index: 5927.
    Returns: the total time Kim's morning routine takes.
    """
    # L1
    minutes_status_update_per_employee = 2 # 2 minutes per employee getting a status update
    minutes_payroll_update_per_employee = 3 # 3 minutes per employee updating payroll records
    minutes_per_employee_total = minutes_status_update_per_employee + minutes_payroll_update_per_employee

    # L2
    num_employees = 9 # 9 employees
    total_employee_update_time = minutes_per_employee_total * num_employees

    # L3
    minutes_making_coffee = 5 # 5 minutes making coffee
    total_morning_routine_time = total_employee_update_time + minutes_making_coffee

    # FA
    answer = total_morning_routine_time
    return answer