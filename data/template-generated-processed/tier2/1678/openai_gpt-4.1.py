def solve():
    """Index: 1678.
    Returns: the additional amount Jackie needs to spend to be eligible for free shipping.
    """
    # L1
    num_shampoo_conditioner = 2 # shampoo and conditioner
    shampoo_conditioner_price = 10 # $10 each
    shampoo_conditioner_total = num_shampoo_conditioner * shampoo_conditioner_price

    # L2
    num_lotion = 3 # 3 bottles of lotion
    lotion_price = 6 # $6 each
    lotion_total = num_lotion * lotion_price

    # L3
    subtotal = shampoo_conditioner_total + lotion_total

    # L4
    free_shipping_threshold = 50 # need to spend $50.00 for free shipping
    amount_needed = free_shipping_threshold - subtotal

    # FA
    answer = amount_needed
    return answer