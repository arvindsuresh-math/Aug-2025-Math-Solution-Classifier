def solve():
    """Index: 1165.
    Returns: the total number of shingles Jerry needs.
    """
    # L1
    roof_side_length_ft_1 = 20 # 20 feet by 40 feet
    roof_side_length_ft_2 = 40 # 20 feet by 40 feet
    area_one_side_sq_ft = roof_side_length_ft_1 * roof_side_length_ft_2

    # L2
    num_slanted_sides_per_roof = 2 # two slanted rectangular sides
    area_both_sides_per_roof_sq_ft = area_one_side_sq_ft * num_slanted_sides_per_roof

    # L3
    num_roofs = 3 # 3 roofs
    total_area_all_roofs_sq_ft = area_both_sides_per_roof_sq_ft * num_roofs

    # L4
    shingles_per_sq_ft = 8 # 8 shingles to cover one square foot of roof
    total_shingles_needed = total_area_all_roofs_sq_ft * shingles_per_sq_ft

    # FA
    answer = total_shingles_needed
    return answer