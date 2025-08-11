from fractions import Fraction

def solve():
    """Index: 2797.
    Returns: the amount of money Mr. Haj pays for the orders done.
    """
    # L1
    total_operation_costs = 4000 # needs $4000 a day
    salary_fraction = Fraction(2, 5) # 2/5 of the total operation costs on employees' salary
    employee_salary = salary_fraction * total_operation_costs

    # L2
    remaining_after_salary = total_operation_costs - employee_salary

    # L3
    delivery_divisor = 4 # 1/4 of the remaining amount on delivery costs
    delivery_costs = remaining_after_salary / delivery_divisor

    # L4
    orders_cost = remaining_after_salary - delivery_costs

    # FA
    answer = orders_cost
    return answer