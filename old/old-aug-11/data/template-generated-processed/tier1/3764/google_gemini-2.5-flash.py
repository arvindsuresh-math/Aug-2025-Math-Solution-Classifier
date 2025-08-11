def solve():
    """Index: 3764.
    Returns: the total weight Lindsey will squat.
    """
    # L1
    num_exercise_bands = 2 # 2 exercise bands
    resistance_per_band = 5 # 5 pounds of resistance
    total_band_resistance = num_exercise_bands * resistance_per_band

    # L2
    dumbbell_weight_per_unit = 10 # a 10-pound dumbbell
    num_dumbbells_used = 2 # WK
    total_dumbbell_weight = num_dumbbells_used * dumbbell_weight_per_unit

    # L3
    total_squat_weight = total_band_resistance + total_dumbbell_weight

    # FA
    answer = total_squat_weight
    return answer