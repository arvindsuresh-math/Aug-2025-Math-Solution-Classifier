def solve():
    """Index: 275.
    Returns: how much more money Gretel will make compared to Hansel after their raises.
    """
    # L1
    base_salary = 30000 # Hansel makes $30,000 a year
    hansel_raise_percent = 0.10 # 10% raise
    hansel_raise_amount = base_salary * hansel_raise_percent

    # L2
    hansel_new_salary = base_salary + hansel_raise_amount

    # L3
    gretel_raise_percent = 0.15 # 15% raise
    gretel_raise_amount = base_salary * gretel_raise_percent

    # L4
    gretel_new_salary = base_salary + gretel_raise_amount

    # L5
    difference = gretel_new_salary - hansel_new_salary

    # FA
    answer = difference
    return answer