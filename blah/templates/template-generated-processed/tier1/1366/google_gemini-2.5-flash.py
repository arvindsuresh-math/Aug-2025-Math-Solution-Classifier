def solve():
    """Index: 1366.
    Returns: the total number of cupcakes baked.
    """
    # L1
    morning_cupcakes = 20 # 20 cupcakes in the morning
    afternoon_additional_cupcakes = 15 # fifteen more cupcakes in the afternoon
    afternoon_cupcakes = morning_cupcakes + afternoon_additional_cupcakes

    # L2
    total_cupcakes = morning_cupcakes + afternoon_cupcakes

    # FA
    answer = total_cupcakes
    return answer