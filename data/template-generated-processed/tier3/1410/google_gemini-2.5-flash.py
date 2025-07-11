def solve():
    """Index: 1410.
    Returns: the number of additional onions Carl can chop in 30 minutes compared to Brittney.
    """
    # L1
    brittney_onions_initial = 15 # Brittney can chop 15 onions
    brittney_time_initial = 5 # in 5 minutes
    brittney_onions_per_minute = brittney_onions_initial / brittney_time_initial

    # L2
    carl_onions_initial = 20 # Carl can chop 20 onions
    carl_time_initial = 5 # within that same time
    carl_onions_per_minute = carl_onions_initial / carl_time_initial

    # L3
    target_time = 30 # in 30 minutes
    brittney_total_onions = brittney_onions_per_minute * target_time

    # L4
    carl_total_onions = carl_onions_per_minute * target_time

    # L5
    difference_in_onions = carl_total_onions - brittney_total_onions

    # FA
    answer = difference_in_onions
    return answer