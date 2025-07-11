def solve():
    """Index: 576.
    Returns: the total number of apples Diane and Cecile bought altogether.
    """
    # L1
    cecile_apples = 15 # Cecile bought 15 apples
    diane_more_than_cecile = 20 # Diane bought twenty more apples than Cecile
    diane_apples = cecile_apples + diane_more_than_cecile

    # L2
    total_apples = cecile_apples + diane_apples

    # FA
    answer = total_apples
    return answer