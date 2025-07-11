def solve():
    """Index: 1241.
    Returns: the weight of the marble statue in kilograms.
    """
    # L1
    base_side = 2 # 2-meter square base
    height = 8 # 8 meters tall
    volume = base_side * base_side * height

    # L2
    density = 2700 # 2700 kg per cubic meter
    weight = density * volume

    # FA
    answer = weight
    return answer