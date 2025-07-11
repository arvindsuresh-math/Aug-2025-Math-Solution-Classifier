def solve():
    """Index: 1888.
    Returns: the number of unused streetlights.
    """
    # L1
    num_squares = 15 # 15 squares in New York
    streetlights_per_square = 12 # each park will have 12 new streetlights
    total_used_streetlights = num_squares * streetlights_per_square

    # L2
    total_bought_streetlights = 200 # bought 200 streetlights
    unused_streetlights = total_bought_streetlights - total_used_streetlights

    # FA
    answer = unused_streetlights
    return answer