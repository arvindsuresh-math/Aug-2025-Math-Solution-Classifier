def solve():
    """Index: 499.
    Returns: the total amount of money Salvadore and Santo earned together.
    """
    # L1
    salvadore_earned = 1956 # Salvadore earned $1956
    santo_fraction = 1/2 # Santo earned half of what Salvadore earned
    santo_earned = santo_fraction * salvadore_earned

    # L2
    total_earned = salvadore_earned + santo_earned

    # FA
    answer = total_earned
    return answer