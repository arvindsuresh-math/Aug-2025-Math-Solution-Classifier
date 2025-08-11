def solve():
    """Index: 5041.
    Returns: the height of the final painting based on the solution's calculation.
    """
    # L1
    painting_side_length = 5 # 5 feet by 5 feet
    area_5x5_painting = painting_side_length * painting_side_length

    # L2
    num_5x5_paintings = 3 # 3 of the paintings
    total_area_5x5_paintings = num_5x5_paintings * area_5x5_painting

    # L3
    painting_10x8_length = 10 # 10 feet by 8 feet
    painting_10x8_width = 8 # 10 feet by 8 feet
    area_10x8_painting = painting_10x8_length * painting_10x8_width

    # L4
    area_first_four_paintings = area_10x8_painting + total_area_5x5_paintings

    # L5
    total_area_all_paintings = 200 # take up 200 square feet
    area_final_painting = total_area_all_paintings - area_first_four_paintings

    # L6
    final_painting_width_given_in_solution = 5 # If it is 5 feet wide
    final_painting_height_calculated = area_final_painting / final_painting_width_given_in_solution

    # FA
    answer = final_painting_height_calculated
    return answer