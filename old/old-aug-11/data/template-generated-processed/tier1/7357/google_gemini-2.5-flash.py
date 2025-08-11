def solve():
    """Index: 7357.
    Returns: the total grams of sand Jason needs.
    """
    # L1
    rectangular_patch_length = 6 # 6 inches by 7 inches
    rectangular_patch_width = 7 # 6 inches by 7 inches
    area_first_patch = rectangular_patch_length * rectangular_patch_width

    # L2
    square_patch_side = 5 # 5 inches by 5 inches
    area_second_patch = square_patch_side * square_patch_side

    # L3
    total_area = area_first_patch + area_second_patch

    # L4
    grams_per_square_inch = 3 # 3 grams of sand to fill one square inch
    total_sand_needed = total_area * grams_per_square_inch

    # FA
    answer = total_sand_needed
    return answer