def solve():
    """Index: 4123.
    Returns: the area, in square feet, for one of the remaining units.
    """
    # L1
    unit_length = 8 # 8 by 4 feet
    unit_width = 4 # 8 by 4 feet
    area_of_small_unit = unit_length * unit_width

    # L2
    num_small_units = 20 # Twenty of the units
    total_area_small_units = num_small_units * area_of_small_unit

    # L3
    total_building_area = 5040 # total of 5040 square feet
    remaining_area = total_building_area - total_area_small_units

    # L4
    total_units = 42 # 42 storage units
    num_remaining_units = total_units - num_small_units

    # L5
    area_per_remaining_unit = remaining_area / num_remaining_units

    # FA
    answer = area_per_remaining_unit
    return answer