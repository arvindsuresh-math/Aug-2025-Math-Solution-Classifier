def solve():
    """Index: 5515.
    Returns: the difference in seconds between the two wait times.
    """
    # L1
    kids_waiting_swings = 3 # 3 kids waiting for the swings
    wait_time_per_kid_swings_minutes = 2 # 2 minutes for the swings
    total_wait_swings_minutes = kids_waiting_swings * wait_time_per_kid_swings_minutes

    # L2
    seconds_per_minute = 60 # WK
    total_wait_swings_seconds = total_wait_swings_minutes * seconds_per_minute

    # L3
    multiplier_slide_kids = 2 # twice as many kids waiting for the slide
    kids_waiting_slide = kids_waiting_swings * multiplier_slide_kids

    # L4
    wait_time_per_kid_slide_seconds = 15 # 15 seconds for the slide
    total_wait_slide_seconds = wait_time_per_kid_slide_seconds * kids_waiting_slide

    # L5
    shorter_wait_difference = total_wait_swings_seconds - total_wait_slide_seconds

    # FA
    answer = shorter_wait_difference
    return answer