def solve():
    """Index: 6923.
    Returns: the total square feet of growing space.
    """
    # L1
    first_bed_length = 3 # 3 ft long
    first_bed_width = 3 # 3 ft wide
    area_first_bed = first_bed_length * first_bed_width

    # L2
    num_first_type_beds = 2 # 2 3 ft long by 3 ft wide garden beds
    total_area_first_type = num_first_type_beds * area_first_bed

    # L3
    second_bed_length = 4 # 4ft long
    second_bed_width = 3 # 3 ft wide
    area_second_bed = second_bed_length * second_bed_width

    # L4
    num_second_type_beds = 2 # 2 4ft long by 3 ft wide garden beds
    total_area_second_type = num_second_type_beds * area_second_bed

    # L5
    total_growing_space = total_area_first_type + total_area_second_type

    # FA
    answer = total_growing_space
    return answer