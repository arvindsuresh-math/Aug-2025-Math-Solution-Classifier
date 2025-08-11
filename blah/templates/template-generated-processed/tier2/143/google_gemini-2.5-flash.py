def solve():
    """Index: 143.
    Returns: the number of goldfish below the surface.
    """
    # L1
    counted_goldfish = 15 # If he counts 15 goldfish
    surface_percentage_decimal = 0.25 # only 25% of goldfish are at the surface
    total_goldfish = counted_goldfish / surface_percentage_decimal

    # L2
    total_percentage_value = 100 # WK
    surface_percentage_value = 25 # 25% of goldfish are at the surface
    below_surface_percentage_value = total_percentage_value - surface_percentage_value

    # L3
    below_surface_percentage_decimal = 0.75 # WK
    goldfish_below_surface = total_goldfish * below_surface_percentage_decimal

    # FA
    answer = goldfish_below_surface
    return answer