def solve():
    """Index: 2122.
    Returns: the number of customers the salon has each day.
    """
    # L1
    total_cans_bought_daily = 33 # salon buys 33 cans of hairspray every day
    surplus_cans_daily = 5 # extra 5 cans of hairspray each day
    cans_for_customers_daily = total_cans_bought_daily - surplus_cans_daily

    # L2
    cans_for_styling_per_customer = 1 # 1 can of hairspray during the styling
    cans_to_take_home_per_customer = 1 # 1 can of hairspray to take home
    total_cans_per_customer = cans_for_styling_per_customer + cans_to_take_home_per_customer

    # L3
    num_customers_daily = cans_for_customers_daily / total_cans_per_customer

    # FA
    answer = num_customers_daily
    return answer