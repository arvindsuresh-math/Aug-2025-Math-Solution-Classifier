def solve():
    """Index: 143.
    Returns: the number of goldfish below the surface.
    """
    # L1
    surface_count = 15 # counts 15 goldfish
    surface_percent_decimal = 0.25 # only 25% of goldfish are at the surface
    total_goldfish = surface_count / surface_percent_decimal

    # L2
    percent_total = 100 # WK
    surface_percent = 25 # only 25% of goldfish are at the surface
    below_surface_percent = percent_total - surface_percent

    # L3
    below_surface_percent_decimal = 0.75 # 75% of the fish are below the surface
    below_surface_count = total_goldfish * below_surface_percent_decimal

    # FA
    answer = below_surface_count
    return answer