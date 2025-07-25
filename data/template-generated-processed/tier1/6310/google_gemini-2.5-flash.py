def solve():
    """Index: 6310.
    Returns: the range of their weights.
    """
    # L1
    jake_more_than_tracy = 8 # 8kg more than Tracy
    tracy_weight = 52 # weighs 52 kg
    jake_weight = jake_more_than_tracy + tracy_weight

    # L2
    tracy_jake_combined_weight = jake_weight + tracy_weight

    # L3
    combined_weight_all = 158 # combined weight to be 158 kilograms
    john_weight = combined_weight_all - tracy_jake_combined_weight

    # L4
    range_of_weights = jake_weight - john_weight

    # FA
    answer = range_of_weights
    return answer