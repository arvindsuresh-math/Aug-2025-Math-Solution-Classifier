def solve():
    """Index: 5635.
    Returns: the number of customers who will go home without any fish.
    """
    # L1
    num_tuna = 10 # 10 tuna
    weight_per_tuna = 200 # each of which weighs 200 pounds
    total_fish_pounds = num_tuna * weight_per_tuna

    # L2
    pounds_per_customer = 25 # Each customer wants 25 pounds of tuna
    customers_served = total_fish_pounds / pounds_per_customer

    # L3
    total_customers = 100 # 100 customers waiting
    customers_without_fish = total_customers - customers_served

    # FA
    answer = customers_without_fish
    return answer