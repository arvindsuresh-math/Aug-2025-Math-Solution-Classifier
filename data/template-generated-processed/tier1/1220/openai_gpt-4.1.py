def solve():
    """Index: 1220.
    Returns: the total height of the three buildings together in feet.
    """
    # L1
    first_building_height = 600 # first building was 600 feet
    second_building_multiplier = 2 # second building being two times as tall as the first building
    second_building_height = first_building_height * second_building_multiplier

    # L2
    total_first_second = second_building_height + first_building_height

    # L3
    third_building_multiplier = 3 # third building had to be three times as tall as the combined height
    third_building_height = total_first_second * third_building_multiplier

    # L4
    total_height = third_building_height + total_first_second

    # FA
    answer = total_height
    return answer