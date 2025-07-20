def solve():
    """Index: 4007.
    Returns: how much Liz's team loses by at the end of the game.
    """
    # L1
    num_free_throws = 5 # sinking 5 free throw shots
    points_per_free_throw = 1 # WK
    liz_free_throw_points = num_free_throws * points_per_free_throw

    # L2
    num_three_pointers = 3 # 3 three-pointers
    points_per_three_pointer = 3 # WK
    liz_three_pointer_points = num_three_pointers * points_per_three_pointer

    # L3
    num_jump_shots = 4 # 4 other jump shots
    points_per_jump_shot = 2 # WK
    liz_jump_shot_points = num_jump_shots * points_per_jump_shot

    # L4
    initial_deficit = 20 # down by 20 points
    opponent_score_quarter = 10 # The other team only scores 10 points that quarter
    opponent_lead_before_liz_score = initial_deficit + opponent_score_quarter

    # L5
    liz_total_points = liz_free_throw_points + liz_three_pointer_points + liz_jump_shot_points

    # L6
    final_loss_margin = opponent_lead_before_liz_score - liz_total_points

    # FA
    answer = final_loss_margin
    return answer