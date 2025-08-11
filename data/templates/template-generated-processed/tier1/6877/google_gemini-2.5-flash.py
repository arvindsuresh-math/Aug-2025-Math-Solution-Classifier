def solve():
    """Index: 6877.
    Returns: the total number of apples in the bowl.
    """
    # L1
    red_apples = 16 # 16 red apples
    more_green_than_red = 12 # 12 more green apples than red apples
    green_apples = red_apples + more_green_than_red

    # L2
    total_apples = green_apples + red_apples

    # FA
    answer = total_apples
    return answer