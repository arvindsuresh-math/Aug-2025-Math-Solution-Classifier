def solve():
    """Index: 5501.
    Returns: the difference between green and red apples after delivery.
    """
    # L1
    more_red_than_green = 200 # 200 more red apples than green apples
    original_green_apples = 32 # originally 32 green apples
    red_apples = more_red_than_green + original_green_apples

    # L2
    delivered_green_apples = 340 # delivers another 340 green apples
    total_green_apples = delivered_green_apples + original_green_apples

    # L3
    difference_green_red = total_green_apples - red_apples

    # FA
    answer = difference_green_red
    return answer