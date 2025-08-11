def solve():
    """Index: 4956.
    Returns: the total square inches of velvet Nathan needs.
    """
    # L1
    long_side_length = 8 # 8 inches by 6 inches
    long_side_width = 6 # 8 inches by 6 inches
    area_long_side = long_side_length * long_side_width

    # L2
    short_side_length = 5 # 5 inches by six inches
    short_side_width = 6 # 5 inches by six inches
    area_short_side = short_side_length * short_side_width

    # L3
    area_top_bottom = 40 # top and a bottom that each measure 40 square inches
    sum_of_one_of_each_side = area_long_side + area_short_side + area_top_bottom

    # L4
    num_of_each_side = 2 # two of each kind of side
    total_velvet_needed = sum_of_one_of_each_side * num_of_each_side

    # FA
    answer = total_velvet_needed
    return answer