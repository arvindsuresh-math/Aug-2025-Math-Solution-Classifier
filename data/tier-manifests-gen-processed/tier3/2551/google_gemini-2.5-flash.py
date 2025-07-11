def solve():
    """Index: 2551.
    Returns: the number of additional three-pointers Duke scored compared to his normal amount.
    """
    # L1
    points_to_tie_record = 17 # needs 17 more points to tie the record
    points_broke_record_by = 5 # breaks the record by 5 points
    duke_final_game_score = points_to_tie_record + points_broke_record_by

    # L2
    num_free_throws = 5 # made 5 free throws
    free_throw_value = 1 # worth one point
    free_throw_points = num_free_throws * free_throw_value

    # L3
    num_regular_baskets = 4 # 4 regular baskets
    regular_basket_value = 2 # worth two points
    regular_basket_points = num_regular_baskets * regular_basket_value

    # L4
    three_pointer_points = duke_final_game_score - free_throw_points - regular_basket_points

    # L5
    three_pointer_value = 3 # some three-pointers
    num_three_pointers_final_game = three_pointer_points / three_pointer_value

    # L6
    normal_three_pointers = 2 # Normally, he scores 2 three-pointers a game
    additional_three_pointers = num_three_pointers_final_game - normal_three_pointers

    # FA
    answer = additional_three_pointers
    return answer