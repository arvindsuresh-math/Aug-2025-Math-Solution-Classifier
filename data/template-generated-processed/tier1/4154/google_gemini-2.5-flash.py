def solve():
    """Index: 4154.
    Returns: the total number of sandstone blocks in the pyramid.
    """
    # L1
    top_layer_blocks = 1 # The top layer is a single block
    multiplier = 3 # three times as many sandstone blocks
    second_layer_blocks = top_layer_blocks * multiplier

    # L2
    third_layer_blocks = second_layer_blocks * multiplier

    # L3
    fourth_layer_blocks = third_layer_blocks * multiplier

    # L4
    total_blocks = top_layer_blocks + second_layer_blocks + third_layer_blocks + fourth_layer_blocks

    # FA
    answer = total_blocks
    return answer