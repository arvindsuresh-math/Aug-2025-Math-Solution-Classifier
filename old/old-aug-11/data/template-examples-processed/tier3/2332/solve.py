def solve():
    """Index: 2332.
    Returns: the radius of the ash cloud in feet.
    """
    # L1
    erupted_height = 300 # erupted three hundred feet
    diameter_multiplier = 18 # diameter eighteen times as far
    ash_cloud_diameter = erupted_height * diameter_multiplier

    # L2
    radius_divisor = 2 # WK
    ash_cloud_radius = ash_cloud_diameter / radius_divisor

    # FA
    answer = ash_cloud_radius
    return answer