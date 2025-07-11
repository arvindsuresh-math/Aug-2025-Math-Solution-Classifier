def solve():
    """Index: 135.
    Returns: the number of square feet in Benedict's house.
    """
    # L1
    kennedy_sqft = 10000 # Kennedy's house is 10000 square feet
    benedict_multiplier = 4 # 4 times Benedict's house
    difference = 600 # 600 square feet larger
    # Equation: benedict_multiplier * x + difference = kennedy_sqft

    # L2
    left_side = kennedy_sqft - difference
    # 4 * x = left_side

    # L3
    benedict_sqft = left_side // benedict_multiplier

    # FA
    answer = benedict_sqft
    return answer