def solve():
    """Index: 1708.
    Returns: the total number of points scored by both teams.
    """
    # L1
    two_pointers_made_mark = 25 # 25 2 pointers
    two_pointer_value = 2 # 2 pointers
    mark_two_pointer_points = two_pointers_made_mark * two_pointer_value

    # L2
    three_pointers_made_mark = 8 # 8 3 pointers
    three_pointer_value = 3 # 3 pointers
    mark_three_pointer_points = three_pointers_made_mark * three_pointer_value

    # L3
    free_throws_made_mark = 10 # 10 free throws
    free_throw_value = 1 # free throws count as one point
    mark_free_throw_points = free_throws_made_mark * free_throw_value

    # L4
    mark_total_points = mark_two_pointer_points + mark_three_pointer_points + mark_free_throw_points

    # L5
    opponent_two_pointer_multiplier = 2 # double the 2 pointers
    opponent_two_pointer_points = mark_two_pointer_points * opponent_two_pointer_multiplier

    # L6
    opponent_three_pointer_divisor = 2 # half the 3 pointers
    opponent_three_pointer_points = mark_three_pointer_points / opponent_three_pointer_divisor

    # L7
    opponent_free_throw_divisor = 2 # half the ... free throws
    opponent_free_throw_points = mark_free_throw_points / opponent_free_throw_divisor

    # L8
    opponent_total_points = opponent_two_pointer_points + opponent_three_pointer_points + opponent_free_throw_points

    # L9
    total_game_score = mark_total_points + opponent_total_points

    # FA
    answer = total_game_score
    return answer