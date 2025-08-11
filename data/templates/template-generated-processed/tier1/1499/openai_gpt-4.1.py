def solve():
    """Index: 1499.
    Returns: the total dollars the taco truck made during the lunch rush.
    """
    # L1
    family_soft = 3 # family buys three soft tacos
    soft_per_customer = 2 # rest of the customers only buy two soft tacos each
    num_customers_after_family = 10 # ten customers after the family
    total_soft = family_soft + soft_per_customer * num_customers_after_family

    # L2
    price_soft = 2 # soft tacos for $2
    soft_revenue = price_soft * total_soft

    # L3
    price_hard = 5 # hard shell tacos for $5
    family_hard = 4 # family buys four hard shell tacos
    hard_revenue = price_hard * family_hard

    # L4
    total_revenue = soft_revenue + hard_revenue

    # FA
    answer = total_revenue
    return answer