def solve():
    """Index: 3226.
    Returns: the total amount of tips Wade made over three days.
    """
    # L1
    friday_customers = 28 # On Friday he served 28 customers
    saturday_multiplier = 3 # three times that amount of customers
    saturday_customers = saturday_multiplier * friday_customers

    # L2
    sunday_customers = 36 # On Sunday, he served 36 customers
    total_customers = friday_customers + saturday_customers + sunday_customers

    # L3
    tip_per_customer = 2.00 # He makes $2.00 in tips per customer
    total_tips = tip_per_customer * total_customers

    # FA
    answer = total_tips
    return answer