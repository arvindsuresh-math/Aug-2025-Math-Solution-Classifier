def solve():
    """Index: 6651.
    Returns: the number of sweets that are neither red nor green.
    """
    # L1
    red_sweets = 49 # 49 of the sweets are red
    green_sweets = 59 # 59 of the sweets are green
    red_or_green_sweets = red_sweets + green_sweets

    # L2
    total_sweets = 285 # 285 sweets in the bowl
    neither_red_nor_green_sweets = total_sweets - red_or_green_sweets

    # FA
    answer = neither_red_nor_green_sweets
    return answer