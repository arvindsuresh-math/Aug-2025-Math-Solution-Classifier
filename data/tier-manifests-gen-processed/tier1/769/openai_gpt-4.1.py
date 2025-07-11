def solve():
    """Index: 769.
    Returns: the number of seconds remaining for the fries to be fully cooked.
    """
    # L1
    recommended_minutes = 5 # recommended time was 5 minutes
    seconds_per_minute = 60 # WK
    total_cook_seconds = recommended_minutes * seconds_per_minute

    # L2
    seconds_cooked = 45 # put them in for 45 seconds
    seconds_remaining = total_cook_seconds - seconds_cooked

    # FA
    answer = seconds_remaining
    return answer