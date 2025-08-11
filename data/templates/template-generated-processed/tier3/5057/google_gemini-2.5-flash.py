def solve():
    """Index: 5057.
    Returns: the number of tomatoes left on the plant.
    """
    # L1
    total_tomatoes = 21 # 21 cherry tomatoes on the tomato plant
    fraction_denominator = 3 # one-third of the tomatoes
    eaten_tomatoes = total_tomatoes / fraction_denominator

    # L2
    remaining_tomatoes = total_tomatoes - eaten_tomatoes

    # FA
    answer = remaining_tomatoes
    return answer