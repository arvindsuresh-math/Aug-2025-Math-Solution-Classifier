def solve():
    """Index: 2332.
    Returns: the radius of the ash cloud in feet.
    """
    # L1
    eruption_height = 300 # three hundred feet into the sky
    diameter_multiplier = 18 # eighteen times as far
    ash_cloud_diameter = eruption_height * diameter_multiplier

    # L2
    radius_divisor = 2 # half the diameter
    ash_cloud_radius = ash_cloud_diameter / radius_divisor

    # FA
    answer = ash_cloud_radius
    return answer