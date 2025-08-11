def solve():
    """Index: 7005.
    Returns: the total value in billions of all the land on the moon.
    """
    # L1
    earth_total_value = 80 # total value of all the land on the earth is 80 billion dollars
    moon_surface_area_ratio_denominator = 5 # surface area that is 1/5 that of Earth
    moon_value_if_same_as_earth = earth_total_value / moon_surface_area_ratio_denominator

    # L2
    moon_land_value_multiplier = 6 # land on the moon is worth 6 times that of the land on the Earth
    total_moon_land_value = moon_value_if_same_as_earth * moon_land_value_multiplier

    # FA
    answer = total_moon_land_value
    return answer