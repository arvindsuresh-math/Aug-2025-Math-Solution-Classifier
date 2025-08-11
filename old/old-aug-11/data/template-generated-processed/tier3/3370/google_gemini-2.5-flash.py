def solve():
    """Index: 3370.
    Returns: the number of customers who bought two watermelons.
    """
    # L1
    melons_per_customer_one_melon_group = 1 # WK
    customers_one_melon_group = 17 # Seventeen customers bought one melon
    total_melons_one_melon_group = melons_per_customer_one_melon_group * customers_one_melon_group

    # L2
    melons_per_customer_three_melon_group = 3 # WK
    customers_three_melon_group = 3 # three customers bought three melons
    total_melons_three_melon_group = melons_per_customer_three_melon_group * customers_three_melon_group

    # L3
    total_melons_sold = 46 # sold 46 watermelons
    melons_bought_by_two_melon_customers = total_melons_sold - total_melons_one_melon_group - total_melons_three_melon_group

    # L4
    melons_per_customer_two_melon_group = 2 # the rest bought two melons
    customers_two_melon_group = melons_bought_by_two_melon_customers / melons_per_customer_two_melon_group

    # FA
    answer = customers_two_melon_group
    return answer