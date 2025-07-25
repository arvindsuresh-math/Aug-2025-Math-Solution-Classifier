def solve():
    """Index: 2139.
    Returns: the total number of dolphins in the ocean after the river dolphins join.
    """
    # L1
    initial_dolphins = 65 # sixty-five dolphins in the ocean
    multiplier = 3 # three times that number joins in
    dolphins_joined = multiplier * initial_dolphins

    # L2
    total_dolphins = dolphins_joined + initial_dolphins

    # FA
    answer = total_dolphins
    return answer