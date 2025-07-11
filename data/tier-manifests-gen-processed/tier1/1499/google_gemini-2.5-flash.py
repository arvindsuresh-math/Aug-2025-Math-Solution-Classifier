def solve():
    """Index: 1499.
    Returns: the total dollars the taco truck made during the lunch rush.
    """
    # L1
    family_soft_tacos = 3 # three soft tacos
    soft_tacos_per_other_customer = 2 # two soft tacos each
    num_other_customers = 10 # ten customers after the family
    soft_tacos_from_other_customers = soft_tacos_per_other_customer * num_other_customers
    total_soft_tacos = family_soft_tacos + soft_tacos_from_other_customers

    # L2
    soft_taco_price = 2 # soft tacos for $2
    revenue_soft_tacos = soft_taco_price * total_soft_tacos

    # L3
    hard_shell_taco_price = 5 # hard shell tacos for $5
    family_hard_shell_tacos = 4 # four hard shell tacos
    revenue_hard_shell_tacos = hard_shell_taco_price * family_hard_shell_tacos

    # L4
    total_revenue = revenue_soft_tacos + revenue_hard_shell_tacos

    # FA
    answer = total_revenue
    return answer