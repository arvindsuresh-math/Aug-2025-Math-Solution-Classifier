def solve():
    """Index: 2066.
    Returns: the total amount the restaurant donates.
    """
    # L1
    customers_that_day = 40 # 40 customers that day
    average_customer_donation = 3 # average customer donates 3
    total_customer_donation = customers_that_day * average_customer_donation

    # L2
    donation_unit = 10 # $10 donated by customers
    num_donation_units = total_customer_donation / donation_unit

    # L3
    restaurant_donation_per_unit = 2 # $2 for every $10 donated
    restaurant_total_donation = num_donation_units * restaurant_donation_per_unit

    # FA
    answer = restaurant_total_donation
    return answer