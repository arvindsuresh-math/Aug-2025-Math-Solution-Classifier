def solve():
    """Index: 6274.
    Returns: the total square feet of sod needed to cover the yard, minus the sidewalk and flower beds.
    """
    # L1
    yard_width = 200 # 200 feet wide
    yard_length = 50 # 50 feet
    yard_area = yard_width * yard_length

    # L2
    sidewalk_width = 3 # 3 feet wide
    sidewalk_length = 50 # 50 feet long
    sidewalk_area = sidewalk_width * sidewalk_length

    # L3
    flower_bed_front_depth = 4 # 4 feet deep
    flower_bed_front_length = 25 # 25 feet long
    single_front_flower_bed_area = flower_bed_front_depth * flower_bed_front_length
    num_front_flower_beds = 2 # two right in front of the house
    total_front_flower_beds_area = num_front_flower_beds * single_front_flower_bed_area

    # L4
    flower_bed_third_width = 10 # 10 feet
    flower_bed_third_length = 12 # 12 feet
    flower_bed_third_area = flower_bed_third_width * flower_bed_third_length

    # L5
    flower_bed_fourth_width = 7 # 7 feet
    flower_bed_fourth_length = 8 # 8 feet
    flower_bed_fourth_area = flower_bed_fourth_width * flower_bed_fourth_length

    # L6
    total_excluded_area = sidewalk_area + total_front_flower_beds_area + flower_bed_third_area + flower_bed_fourth_area

    # L7
    sod_needed = yard_area - total_excluded_area

    # FA
    answer = sod_needed
    return answer