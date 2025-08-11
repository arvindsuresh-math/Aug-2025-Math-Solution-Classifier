def solve():
    """Index: 5117.
    Returns: the total number of apartment units Mr. Resty has.
    """
    # L1
    total_stories = 4 # 4-story buildings
    first_floor_count = 1 # first floor
    floors_with_five_units = total_stories - first_floor_count

    # L2
    units_per_other_floor = 5 # rest of the floors have 5 apartment units
    units_from_other_floors_per_building = floors_with_five_units * units_per_other_floor

    # L3
    first_floor_units = 2 # The first floor has 2 apartment units
    total_units_per_building = units_from_other_floors_per_building + first_floor_units

    # L4
    num_buildings = 2 # two identical 4-story buildings
    total_units_all_buildings = total_units_per_building * num_buildings

    # FA
    answer = total_units_all_buildings
    return answer