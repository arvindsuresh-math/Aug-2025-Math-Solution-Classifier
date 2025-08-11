def solve():
    """Index: 5911.
    Returns: the total height of the building.
    """
    # L1
    total_floors = 20 # A building has 20 floors
    special_floors_count = 2 # last two floors
    standard_floors_count = total_floors - special_floors_count

    # L2
    standard_floor_height = 3 # Each floor is 3 meters high
    height_standard_floors = standard_floors_count * standard_floor_height

    # L3
    extra_height_per_special_floor = 0.5 # each 0.5 meters higher
    special_floor_height = standard_floor_height + extra_height_per_special_floor

    # L4
    height_special_floors = special_floor_height * special_floors_count

    # L5
    total_building_height = height_standard_floors + height_special_floors

    # FA
    answer = total_building_height
    return answer