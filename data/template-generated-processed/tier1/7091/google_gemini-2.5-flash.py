def solve():
    """Index: 7091.
    Returns: the total number of bike clamps given away by the store.
    """
    # L1
    bikes_morning = 19 # 19 bikes in the morning
    clamps_per_bike = 2 # 2 bike clamps free
    clamps_morning = bikes_morning * clamps_per_bike

    # L2
    bikes_afternoon = 27 # 27 bikes in the afternoon
    clamps_afternoon = bikes_afternoon * clamps_per_bike

    # L3
    total_clamps = clamps_morning + clamps_afternoon

    # FA
    answer = total_clamps
    return answer