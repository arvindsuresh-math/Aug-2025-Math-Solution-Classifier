def solve():
    """Index: 5412.
    Returns: the amount of water left over in milliliters.
    """
    # L1
    initial_liters = 8 # 8 liters of water
    ml_per_liter = 1000 # WK
    initial_ml_water = initial_liters * ml_per_liter

    # L2
    ml_per_player = 200 # 200 milliliters of water for every player
    num_players = 30 # 30 players on a football team
    total_poured_ml = ml_per_player * num_players

    # L3
    spilled_ml = 250 # 250ml of water was spilled
    total_water_used = total_poured_ml + spilled_ml

    # L4
    water_left_over = initial_ml_water - total_water_used

    # FA
    answer = water_left_over
    return answer