def solve():
    """Index: 4267.
    Returns: the number of views the video had gained on Youtube.
    """
    # L1
    views_first_day = 4000 # 4000 views on the first day
    increase_multiplier = 10 # ten times more than the views on the first day
    views_increased_after_four_days = increase_multiplier * views_first_day

    # L2
    total_views_after_four_days = views_increased_after_four_days + views_first_day

    # L3
    additional_views_after_two_days = 50000 # 50000 more people viewed the video after another two days
    final_total_views = total_views_after_four_days + additional_views_after_two_days

    # FA
    answer = final_total_views - views_first_day
    return answer