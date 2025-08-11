def solve():
    """Index: 2769.
    Returns: the cost of each ring in dollars.
    """
    # L2
    num_necklaces = 4 # sold 4 necklaces
    necklace_cost = 12 # each necklace costs $12
    num_rings = 8 # sold 8 rings
    total_sales = 80 # total of $80
    # 4*12+8*r=80
    # L4
    necklaces_total = num_necklaces * necklace_cost
    rings_total = total_sales - necklaces_total
    # L5
    # 8r=32
    # L6
    ring_cost = rings_total // num_rings
    # FA
    answer = ring_cost
    return answer