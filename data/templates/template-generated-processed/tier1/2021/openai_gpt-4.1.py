def solve():
    """Index: 2021.
    Returns: the total number of fruit salads in the two restaurants.
    """
    # L1
    angel_multiplier = 2 # twice the number of fruit salads
    alaya_salads = 200 # Alaya's restaurant has 200 fruit salads
    angel_salads = angel_multiplier * alaya_salads

    # L2
    total_salads = alaya_salads + angel_salads

    # FA
    answer = total_salads
    return answer