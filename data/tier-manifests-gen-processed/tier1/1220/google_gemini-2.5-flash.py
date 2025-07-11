def solve():
    """Index: 1220.
    Returns: the total height of the three buildings together.
    """
    # L1
    first_building_height = 600 # first building was 600 feet
    multiplier_second_building = 2 # two times as tall as the first building
    second_building_height = first_building_height * multiplier_second_building

    # L2
    combined_height_first_second = second_building_height + first_building_height

    # L3
    multiplier_third_building = 3 # three times as tall as the combined height
    third_building_height = combined_height_first_second * multiplier_third_building

    # L4
    total_height_three_buildings = third_building_height + combined_height_first_second

    # FA
    answer = total_height_three_buildings
    return answer