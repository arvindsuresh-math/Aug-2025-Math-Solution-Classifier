def solve():
    """Index: 769.
    Returns: the number of seconds remaining for the french fries to be fully cooked.
    """
    # L1
    recommended_minutes = 5 # 5 minutes for them to be fully cooked
    seconds_per_minute = 60 # WK
    total_required_seconds = recommended_minutes * seconds_per_minute

    # L2
    cooked_seconds = 45 # put them in for 45 seconds
    remaining_seconds = total_required_seconds - cooked_seconds

    # FA
    answer = remaining_seconds
    return answer