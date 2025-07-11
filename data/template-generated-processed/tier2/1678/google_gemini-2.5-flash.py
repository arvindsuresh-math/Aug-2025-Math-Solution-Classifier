def solve():
    """Index: 1678.
    Returns: how much more money Jackie needs to spend to be eligible for free shipping.
    """
    # L1
    num_shampoo_conditioner_bottles = 2 # shampoo and conditioner
    shampoo_conditioner_cost_per_bottle = 10.00 # each cost $10.00 a bottle
    shampoo_conditioner_total_cost = num_shampoo_conditioner_bottles * shampoo_conditioner_cost_per_bottle

    # L2
    num_lotion_bottles = 3 # 3 bottles of lotion
    lotion_cost_per_bottle = 6.00 # cost $6.00 each
    lotion_total_cost = num_lotion_bottles * lotion_cost_per_bottle

    # L3
    current_spent_total = shampoo_conditioner_total_cost + lotion_total_cost

    # L4
    free_shipping_threshold = 50.00 # free shipping when you spent $50.00
    money_needed_for_free_shipping = free_shipping_threshold - current_spent_total

    # FA
    answer = money_needed_for_free_shipping
    return answer