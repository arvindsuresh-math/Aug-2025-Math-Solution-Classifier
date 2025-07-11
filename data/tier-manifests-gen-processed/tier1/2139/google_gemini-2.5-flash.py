def solve():
    """Index: 2139.
    Returns: the total number of dolphins in the ocean.
    """
    # L1
    multiplier = 3 # three times that number
    initial_dolphins = 65 # sixty-five dolphins in the ocean
    dolphins_from_river = multiplier * initial_dolphins

    # L2
    total_dolphins = dolphins_from_river + initial_dolphins

    # FA
    answer = total_dolphins
    return answer