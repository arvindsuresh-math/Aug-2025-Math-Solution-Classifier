def solve():
    """Index: 1366.
    Returns: the total number of cupcakes Ivy baked.
    """
    # L1
    morning_cupcakes = 20 # baked 20 cupcakes in the morning
    afternoon_more_than_morning = 15 # fifteen more cupcakes in the afternoon than in the morning
    afternoon_cupcakes = morning_cupcakes + afternoon_more_than_morning

    # L2
    total_cupcakes = morning_cupcakes + afternoon_cupcakes

    # FA
    answer = total_cupcakes
    return answer