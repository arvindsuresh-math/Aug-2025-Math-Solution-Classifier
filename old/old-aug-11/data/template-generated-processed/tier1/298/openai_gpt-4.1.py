def solve():
    """Index: 298.
    Returns: the number of sweets on the table at first.
    """
    # L1
    paul_took = 7 # Paul came and took the remaining 7 sweets
    jack_extra = 4 # Jack took ... and 4 more candies
    half_candies = paul_took + jack_extra

    # L2
    multiplier_for_half = 2 # half of all the candies
    total_candies = half_candies * multiplier_for_half

    # FA
    answer = total_candies
    return answer