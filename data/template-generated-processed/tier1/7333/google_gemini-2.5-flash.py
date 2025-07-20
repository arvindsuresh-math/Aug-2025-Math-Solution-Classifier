def solve():
    """Index: 7333.
    Returns: the total money spent after buying the lightsaber.
    """
    # L1
    other_toys_cost = 1000 # his other Star Wars toys cost $1000
    multiplier_lightsaber = 2 # twice as expensive
    lightsaber_cost = other_toys_cost * multiplier_lightsaber

    # L2
    total_spent = lightsaber_cost + other_toys_cost

    # FA
    answer = total_spent
    return answer