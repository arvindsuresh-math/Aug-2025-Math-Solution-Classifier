def solve():
    """Index: 1304.
    Returns: the total amount Julio earns for the 3 weeks.
    """
    # L1
    customers_week1 = 35 # sells to 35 customers in the first week
    multiplier_week2 = 2 # twice as many in the second week
    customers_week2 = customers_week1 * multiplier_week2

    # L2
    multiplier_week3 = 3 # triple as many as the first week in the third week
    customers_week3 = customers_week1 * multiplier_week3

    # L3
    total_customers = customers_week1 + customers_week2 + customers_week3

    # L4
    commission_per_customer = 1 # $1 commission for every customer
    total_commission = total_customers * commission_per_customer

    # L5
    salary = 500 # receives a salary of $500 for the 3 weeks
    bonus = 50 # and a bonus of $50
    total_income = total_commission + salary + bonus

    # FA
    answer = total_income
    return answer