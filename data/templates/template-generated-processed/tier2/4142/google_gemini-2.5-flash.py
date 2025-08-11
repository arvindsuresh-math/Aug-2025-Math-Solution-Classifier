def solve():
    """Index: 4142.
    Returns: Quinten's estimated total height of the three buildings.
    """
    # L1
    middle_building_height = 100 # the one in the middle is 100 feet tall
    left_building_ratio = 0.8 # 80% of the height of the middle one
    left_building_height = middle_building_height * left_building_ratio

    # L2
    combined_left_middle_height = middle_building_height + left_building_height

    # L3
    right_building_shorter_amount = 20 # 20 feet shorter
    right_building_height = combined_left_middle_height - right_building_shorter_amount

    # L4
    total_height = left_building_height + middle_building_height + right_building_height

    # FA
    answer = total_height
    return answer