def solve():
    """Index: 695.
    Returns: the number of 150 ml servings Carla can make.
    """
    # L1
    watermelon_puree_volume = 500 # 500 ml of watermelon puree
    cream_volume = 100 # 100 ml of cream
    total_volume = watermelon_puree_volume + cream_volume

    # L2
    serving_volume = 150 # 150 ml servings
    number_of_servings = total_volume / serving_volume

    # FA
    answer = number_of_servings
    return answer