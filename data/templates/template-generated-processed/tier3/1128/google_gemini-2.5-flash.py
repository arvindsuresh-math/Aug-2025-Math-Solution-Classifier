def solve():
    """Index: 1128.
    Returns: the number of gilled mushrooms on the fallen log's side.
    """
    # L1
    gilled_ratio_numerator = 1 # one growing for every nine spotted mushrooms
    spotted_ratio = 9 # nine spotted mushrooms
    total_ratio_parts = gilled_ratio_numerator + spotted_ratio

    # L2
    total_mushrooms = 30 # 30 mushrooms growing on its side
    gilled_mushrooms = total_mushrooms / total_ratio_parts

    # FA
    answer = gilled_mushrooms
    return answer