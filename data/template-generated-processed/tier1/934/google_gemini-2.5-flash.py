def solve():
    """Index: 934.
    Returns: the total number of turtles received by Marion and Martha together.
    """
    # L1
    marion_more_than_martha = 20 # 20 more turtles than Martha
    martha_turtles = 40 # Martha received 40 turtles
    marion_turtles = marion_more_than_martha + martha_turtles

    # L2
    total_turtles = marion_turtles + martha_turtles

    # FA
    answer = total_turtles
    return answer