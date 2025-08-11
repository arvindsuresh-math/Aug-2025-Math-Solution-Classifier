def solve():
    """Index: 2980.
    Returns: the number of bowls remaining in the rewards collection.
    """
    # L1
    total_customers = 20 # 20 customers that day
    half_numerator = 1 # Half of the 20 customers
    half_denominator = 2 # Half of the 20 customers
    customers_bought_20_bowls = (half_numerator / half_denominator) * total_customers

    # L2
    rewards_per_unit_bought = 2 # rewards two to his customers for every 10 they buy
    rewards_per_customer_buying_20_bowls = rewards_per_unit_bought + rewards_per_unit_bought

    # L3
    total_rewards_given = rewards_per_customer_buying_20_bowls * customers_bought_20_bowls

    # L4
    initial_bowls_collection = 70 # collection of 70 wooden bowls
    remaining_bowls = initial_bowls_collection - total_rewards_given

    # FA
    answer = remaining_bowls
    return answer