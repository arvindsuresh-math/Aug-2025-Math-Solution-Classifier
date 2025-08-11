def solve():
    """Index: 779.
    Returns: the total cost to plant the flowers.
    """
    # L1
    flower_cost = 9 # flowers cost $9
    clay_pot_more = 20 # clay pot costs $20 more than the flower
    clay_pot_cost = clay_pot_more + flower_cost

    # L2
    soil_less = 2 # bag of soil costs $2 less than the flower
    soil_cost = flower_cost - soil_less

    # L3
    total_cost = flower_cost + clay_pot_cost + soil_cost

    # FA
    answer = total_cost
    return answer