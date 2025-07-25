def solve():
    """Index: 6633.
    Returns: the total money Dennis will have to spend after the discount.
    """
    # L1
    num_pants_pairs = 4 # 4 pairs of pants
    cost_per_pant_pair = 110 # $110.00 each
    total_pants_cost = cost_per_pant_pair * num_pants_pairs

    # L2
    num_socks_pairs = 2 # 2 pairs of socks
    cost_per_sock_pair = 60 # $60.00
    total_socks_cost = cost_per_sock_pair * num_socks_pairs

    # L3
    subtotal_cost = total_pants_cost + total_socks_cost

    # L4
    discount_rate = 0.30 # 30% discount
    discount_amount = subtotal_cost * discount_rate

    # L5
    final_cost = subtotal_cost - discount_amount

    # FA
    answer = final_cost
    return answer