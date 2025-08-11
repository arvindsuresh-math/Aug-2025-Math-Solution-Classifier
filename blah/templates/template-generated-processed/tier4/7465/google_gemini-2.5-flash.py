def solve():
    """Index: 7465.
    Returns: James's new body weight.
    """
    # L1
    initial_weight = 120 # He weighs 120 kg
    muscle_gain_percent = 0.2 # gains 20% of his body weight
    muscle_gain_kg = initial_weight * muscle_gain_percent

    # L2
    fat_gain_fraction_divisor = 4 # 1 quarter that much in fat
    fat_gain_kg = muscle_gain_kg / fat_gain_fraction_divisor

    # L3
    total_gain_kg = muscle_gain_kg + fat_gain_kg

    # L4
    new_weight = initial_weight + total_gain_kg

    # FA
    answer = new_weight
    return answer