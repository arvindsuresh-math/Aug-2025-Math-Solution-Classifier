def solve():
    """Index: 2523.
    Returns: the total amount Jim is out of pocket.
    """
    # L1
    first_ring_cost = 10000 # Jim buys a wedding ring for $10,000
    multiplier = 2 # twice that much
    second_ring_cost = multiplier * first_ring_cost

    # L2
    sale_divisor = 2 # sells the first one for half its value
    first_ring_sale_value = first_ring_cost / sale_divisor

    # L3
    out_of_pocket_first_ring = first_ring_cost - first_ring_sale_value

    # L4
    total_out_of_pocket = second_ring_cost + out_of_pocket_first_ring

    # FA
    answer = total_out_of_pocket
    return answer