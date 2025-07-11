def solve():
    """Index: 2243.
    Returns: the total number of flowers sold on Tuesday.
    """
    # L1
    lilacs_sold = 10 # 10 lilacs
    roses_multiplier = 3 # three times more roses
    roses_sold = roses_multiplier * lilacs_sold

    # L2
    gardenias_divisor = 2 # Half as many gardenias
    gardenias_sold = lilacs_sold / gardenias_divisor

    # L3
    total_flowers_sold = lilacs_sold + roses_sold + gardenias_sold

    # FA
    answer = total_flowers_sold
    return answer