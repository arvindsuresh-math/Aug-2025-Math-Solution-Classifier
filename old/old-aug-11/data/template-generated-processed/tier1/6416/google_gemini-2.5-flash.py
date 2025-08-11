def solve():
    """Index: 6416.
    Returns: the number of steps forward Frank is from his original starting point.
    """
    # L1
    initial_back_steps = 5 # 5 steps back
    initial_forward_steps = 10 # 10 steps forward
    current_position_after_first_moves = initial_forward_steps - initial_back_steps

    # L2
    second_back_steps = 2 # 2 steps back
    current_position_after_second_back = current_position_after_first_moves - second_back_steps

    # L3
    double_factor = 2 # double that amount
    third_forward_steps = double_factor * second_back_steps

    # L4
    final_position = current_position_after_second_back + third_forward_steps

    # FA
    answer = final_position
    return answer