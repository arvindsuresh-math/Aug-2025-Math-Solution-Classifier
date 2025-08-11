def solve():
    """Index: 576.
    Returns: the total number of apples bought by Diane and Cecile.
    """
    # L1
    cecile_apples = 15 # Cecile bought 15 apples
    diane_more_than_cecile = 20 # twenty more apples than Cecile
    diane_apples = cecile_apples + diane_more_than_cecile

    # L2
    total_apples = cecile_apples + diane_apples

    # FA
    answer = total_apples
    return answer