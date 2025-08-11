def solve():
    """Index: 5720.
    Returns: the total number of ladies on the two floors.
    """
    # L1
    ladies_first_floor = 100 # a hundred ladies on the first-floor
    multiplier_party = 3 # three times that many girls
    girls_at_party = multiplier_party * ladies_first_floor

    # L2
    total_ladies = ladies_first_floor + girls_at_party

    # FA
    answer = total_ladies
    return answer