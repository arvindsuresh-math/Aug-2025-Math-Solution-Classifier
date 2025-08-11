def solve():
    """Index: 3769.
    Returns: the number of square feet of fabric Darnell has left.
    """
    # L1
    square_flag_side = 4 # 4 feet by 4 feet
    fabric_per_square_flag = square_flag_side * square_flag_side

    # L2
    wide_flag_length = 5 # 5 feet by 3 feet
    wide_flag_width = 3 # 5 feet by 3 feet
    fabric_per_wide_flag = wide_flag_length * wide_flag_width

    # L3
    tall_flag_length = 3 # 3 feet by 5 feet
    tall_flag_width = 5 # 3 feet by 5 feet
    fabric_per_tall_flag = tall_flag_width * tall_flag_length

    # L4
    num_square_flags = 16 # already made 16 square flags
    total_fabric_square_flags = num_square_flags * fabric_per_square_flag

    # L5
    num_wide_flags = 20 # 20 wide flags
    total_fabric_wide_flags = num_wide_flags * fabric_per_wide_flag

    # L6
    num_tall_flags = 10 # 10 tall flags
    total_fabric_tall_flags = num_tall_flags * fabric_per_tall_flag

    # L7
    total_fabric_used = total_fabric_square_flags + total_fabric_wide_flags + total_fabric_tall_flags

    # L8
    initial_fabric = 1000 # 1000 square feet of fabric
    fabric_left = initial_fabric - total_fabric_used

    # FA
    answer = fabric_left
    return answer