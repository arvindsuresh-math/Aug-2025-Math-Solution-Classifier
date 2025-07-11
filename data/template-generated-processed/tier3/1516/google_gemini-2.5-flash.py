def solve():
    """Index: 1516.
    Returns: the total amount of money Lucille spends on employee salary.
    """
    # L1
    salary_ratio_part = 4 # ratio of 4:11
    stock_ratio_part = 11 # ratio of 4:11
    total_ratio_parts = salary_ratio_part + stock_ratio_part

    # L2
    revenue = 3000 # $3000 as her revenue
    employee_salary = (salary_ratio_part / total_ratio_parts) * revenue

    # FA
    answer = employee_salary
    return answer