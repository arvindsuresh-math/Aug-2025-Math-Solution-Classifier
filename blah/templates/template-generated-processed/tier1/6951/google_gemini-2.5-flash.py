def solve():
    """Index: 6951.
    Returns: the square feet of storage space still available in the building.
    """
    # L1
    boxes_sf = 5000 # 5,000 square feet of storage space
    second_floor_fraction_denominator = 4 # one-quarter of the second floor storage space
    second_floor_total_sf = boxes_sf * second_floor_fraction_denominator

    # L2
    first_floor_multiplier = 2 # twice as much floor space
    first_floor_total_sf = second_floor_total_sf * first_floor_multiplier

    # L3
    total_building_sf = second_floor_total_sf + first_floor_total_sf

    # L4
    available_sf = total_building_sf - boxes_sf

    # FA
    answer = available_sf
    return answer