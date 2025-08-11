def solve():
    """Index: 2286.
    Returns: the number of hours Marta has worked.
    """
    # L1
    collected_total = 240 # collected $240
    tips_collected = 50 # collected $50 in tips
    earned_without_tips = collected_total - tips_collected

    # L2
    hourly_rate = 10 # receives $10
    hours_worked = earned_without_tips / hourly_rate

    # FA
    answer = hours_worked
    return answer