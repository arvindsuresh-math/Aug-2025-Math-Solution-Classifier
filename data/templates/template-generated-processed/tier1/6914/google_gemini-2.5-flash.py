def solve():
    """Index: 6914.
    Returns: the total number of videos Billy watches.
    """
    # L1
    suggestions_per_list = 15 # 15 suggestions
    num_attempts = 5 # a total of 5 times
    total_videos_generated = suggestions_per_list * num_attempts

    # L2
    picked_show_rank = 5 # picks the 5th show suggested on the final suggestion list
    shows_not_considered = suggestions_per_list - picked_show_rank

    # L3
    final_show_number = total_videos_generated - shows_not_considered

    # FA
    answer = final_show_number
    return answer