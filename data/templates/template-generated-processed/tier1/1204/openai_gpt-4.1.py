def solve():
    """Index: 1204.
    Returns: the total number of solar systems and planets in the galaxy.
    """
    # L1
    solar_systems_more_per_planet = 8 # 8 more solar systems for every planet
    base_per_planet = 1 # for every planet (the planet itself)
    solar_systems_per_planet = solar_systems_more_per_planet + base_per_planet

    # L2
    num_planets = 20 # 20 planets in the galaxy
    num_solar_systems = num_planets * solar_systems_per_planet

    # L3
    total = num_solar_systems + num_planets

    # FA
    answer = total
    return answer