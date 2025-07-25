def solve():
    """Index: 367.
    Returns: Emily's new salary after raising all employees to $35,000 per year.
    """
    # L1
    target_salary = 35000 # all of her employees make $35,000 per year
    current_salary = 20000 # employees who make $20,000 per year
    extra_per_employee = target_salary - current_salary

    # L2
    num_employees = 10 # 10 employees
    total_extra = extra_per_employee * num_employees

    # L3
    emily_original_salary = 1000000 # Emily makes $1,000,000 per year
    emily_new_salary = emily_original_salary - total_extra

    # FA
    answer = emily_new_salary
    return answer