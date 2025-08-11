def solve():
    """Index: 2137.
    Returns: the number of tomatoes that grew in Grandpa's absence.
    """
    # L2
    initial_tomatoes = 36 # Grandpa had counted 36 small tomatoes before going on vacation
    multiplier = 100 # counted 100 times more tomatoes
    total_tomatoes = multiplier * initial_tomatoes

    # L3
    tomatoes_grown = total_tomatoes - initial_tomatoes

    # FA
    answer = tomatoes_grown
    return answer