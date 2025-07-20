def solve():
    """Index: 6813.
    Returns: the total height of all four buildings.
    """
    # L1
    first_building_height = 100 # 100 feet tall
    half_divisor = 2 # half that tall
    second_building_height = first_building_height / half_divisor

    # L2
    third_building_height = second_building_height / half_divisor

    # L3
    fifth_divisor = 5 # one-fifth as tall
    fourth_building_height = third_building_height / fifth_divisor

    # L4
    total_height = first_building_height + second_building_height + third_building_height + fourth_building_height

    # FA
    answer = total_height
    return answer