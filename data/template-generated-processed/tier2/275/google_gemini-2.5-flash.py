def solve():
    """Index: 275.
    Returns: the difference in annual earnings between Gretel and Hansel.
    """
    # L1
    hansel_initial_salary = 30000 # Hansel makes $30,000 a year
    hansel_raise_percent_num = 10 # received a 10% raise
    hansel_raise_percent_decimal = 0.10 # received a 10% raise
    hansel_raise_amount = hansel_initial_salary * hansel_raise_percent_decimal

    # L2
    hansel_new_salary = hansel_initial_salary + hansel_raise_amount

    # L3
    gretel_initial_salary = 30000 # Gretel makes the same amount as Hansel
    gretel_raise_percent_num = 15 # received a 15% raise
    gretel_raise_percent_decimal = 0.15 # received a 15% raise
    gretel_raise_amount = gretel_initial_salary * gretel_raise_percent_decimal

    # L4
    gretel_new_salary = gretel_initial_salary + gretel_raise_amount

    # L5
    gretel_more_money = gretel_new_salary - hansel_new_salary

    # FA
    answer = gretel_more_money
    return answer