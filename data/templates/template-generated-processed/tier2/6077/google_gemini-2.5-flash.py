def solve():
    """Index: 6077.
    Returns: the total cost Jezebel will pay for the flowers.
    """
    # L1
    num_dozens_roses = 2 # two dozens of red roses
    roses_per_dozen = 12 # WK
    total_red_roses = num_dozens_roses * roses_per_dozen

    # L2
    cost_per_red_rose = 1.50 # Each red rose costs $1.50
    cost_red_roses = total_red_roses * cost_per_red_rose

    # L3
    num_sunflowers = 3 # 3 pieces of sunflowers
    cost_per_sunflower = 3 # each sunflower costs $3
    cost_sunflowers = num_sunflowers * cost_per_sunflower

    # L4
    total_cost = cost_red_roses + cost_sunflowers

    # FA
    answer = total_cost
    return answer