def solve():
    """Index: 5806.
    Returns: the total number of ice cube trays Dylan needs to fill.
    """
    # L1
    glass_ice_cubes = 8 # 8 ice cubes in his glass
    pitcher_multiplier = 2 # two times as many ice cubes
    pitcher_ice_cubes = glass_ice_cubes * pitcher_multiplier

    # L2
    total_ice_cubes_used = pitcher_ice_cubes + glass_ice_cubes

    # L3
    spaces_per_tray = 12 # 12 spaces each for ice cubes
    total_trays_needed = total_ice_cubes_used / spaces_per_tray

    # FA
    answer = total_trays_needed
    return answer