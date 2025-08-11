def solve():
    """Index: 5822.
    Returns: the predicted number of customers on Saturday.
    """
    # L1
    breakfast_customers = 73 # 73 customers
    lunch_customers = 127 # 127 customers
    dinner_customers = 87 # 87 customers
    total_customers_friday = breakfast_customers + lunch_customers + dinner_customers

    # L2
    multiplier_saturday = 2 # twice the amount of customers
    predicted_customers_saturday = total_customers_friday * multiplier_saturday

    # FA
    answer = predicted_customers_saturday
    return answer