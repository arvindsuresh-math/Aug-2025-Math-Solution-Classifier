def solve():
    """Index: 5055.
    Returns: the total cups of sugar needed for the third layer.
    """
    # L1
    smallest_layer_sugar = 2 # 2 cups of sugar
    multiplier_second_layer = 2 # twice as big as the first
    second_layer_sugar = smallest_layer_sugar * multiplier_second_layer

    # L2
    multiplier_third_layer = 3 # three times larger than the second
    third_layer_sugar = second_layer_sugar * multiplier_third_layer

    # FA
    answer = third_layer_sugar
    return answer