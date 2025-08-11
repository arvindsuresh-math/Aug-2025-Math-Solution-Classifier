def solve():
    """Index: 2021.
    Returns: the total number of fruit salads in the two restaurants.
    """
    # L1
    multiplier_for_angel = 2 # twice the number
    alaya_salads = 200 # Alaya's restaurant has 200 fruit salads
    angel_salads = multiplier_for_angel * alaya_salads

    # L2
    total_salads = alaya_salads + angel_salads

    # FA
    answer = total_salads
    return answer