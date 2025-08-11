def solve():
    """Index: 4576.
    Returns: the total number of drum stick sets Carter goes through.
    """
    # L1
    sets_used_per_show = 5 # 5 sets of drum sticks per show
    sets_tossed_per_show = 6 # tosses 6 new drum stick sets to audience members
    total_sets_per_night = sets_used_per_show + sets_tossed_per_show

    # L2
    num_nights = 30 # 30 nights straight
    total_sets_needed = total_sets_per_night * num_nights

    # FA
    answer = total_sets_needed
    return answer