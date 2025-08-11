def solve():
    """Index: 779.
    Returns: the total cost to plant the flowers.
    """
    # L1
    pot_more_than_flower = 20 # $20 more than the flower
    flowers_cost = 9 # The flowers cost $9
    clay_pot_cost = pot_more_than_flower + flowers_cost

    # L2
    soil_less_than_flower = 2 # $2 less than the flower
    soil_cost = flowers_cost - soil_less_than_flower

    # L3
    total_cost = flowers_cost + clay_pot_cost + soil_cost

    # FA
    answer = total_cost
    return answer