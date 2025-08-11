def solve():
    """Index: 4955.
    Returns: the total daily salary of all employees of the grocery store.
    """
    # L1
    manager_salary_per_day = 5 # daily salary of the manager is $5
    num_managers = 2 # 2 managers
    managers_total_daily_salary = manager_salary_per_day * num_managers

    # L2
    clerk_salary_per_day = 2 # clerk is $2
    num_clerks = 3 # 3 clerks
    clerks_total_daily_salary = num_clerks * clerk_salary_per_day

    # L3
    total_daily_salary = managers_total_daily_salary + clerks_total_daily_salary

    # FA
    answer = total_daily_salary
    return answer