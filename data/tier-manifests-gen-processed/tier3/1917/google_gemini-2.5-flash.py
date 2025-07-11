def solve():
    """Index: 1917.
    Returns: the secretary's new salary.
    """
    # L1
    monthly_salary = 10000 # earns €10,000 a month
    increase_percentage_value = 2 # salary increase of 2%
    percentage_divisor = 100 # WK
    salary_increase_amount = monthly_salary * increase_percentage_value / percentage_divisor

    # L2
    new_salary = monthly_salary + salary_increase_amount

    # FA
    answer = new_salary
    return answer