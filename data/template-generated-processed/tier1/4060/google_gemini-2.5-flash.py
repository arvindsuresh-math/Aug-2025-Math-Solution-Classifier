def solve():
    """Index: 4060.
    Returns: the square meters of the playground not covered by the maintenance building.
    """
    # L1
    side_length_playground = 12 # side length of 12 meters
    area_playground = side_length_playground * side_length_playground

    # L2
    building_length = 8 # measures 8 meters by 5 meters
    building_width = 5 # measures 8 meters by 5 meters
    area_building = building_length * building_width

    # L3
    uncovered_area = area_playground - area_building

    # FA
    answer = uncovered_area
    return answer