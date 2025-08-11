def solve():
    """Index: 6675.
    Returns: the total amount James paid for the t-shirts.
    """
    # L1
    original_shirt_cost = 20 # They each cost $20
    discount_percent = 0.5 # 50% off
    cost_per_shirt_after_sale = original_shirt_cost * discount_percent

    # L2
    num_tshirts = 6 # 6 t-shirts
    total_paid = cost_per_shirt_after_sale * num_tshirts

    # FA
    answer = total_paid
    return answer