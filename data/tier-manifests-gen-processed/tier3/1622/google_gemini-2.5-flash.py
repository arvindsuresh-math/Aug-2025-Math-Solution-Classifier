def solve():
    """Index: 1622.
    Returns: the number of lemons Jose will need.
    """
    # L1
    tablespoons_per_dozen = 12 # 12 tablespoons of lemon juice to make a dozen
    num_dozens = 3 # 3 dozen cupcakes
    total_tablespoons_needed = tablespoons_per_dozen * num_dozens

    # L2
    tablespoons_per_lemon = 4 # Every lemon provides 4 tablespoons of lemon juice
    lemons_needed = total_tablespoons_needed / tablespoons_per_lemon

    # FA
    answer = lemons_needed
    return answer