def solve():
    """Index: 2148.
    Returns: the total time Missy spends watching TV in minutes.
    """
    # L1
    num_reality_shows = 5 # 5 28-minute reality shows
    minutes_per_reality_show = 28 # 28-minute reality shows
    total_reality_minutes = num_reality_shows * minutes_per_reality_show

    # L2
    cartoon_minutes = 10 # one 10-minute cartoon
    total_minutes = total_reality_minutes + cartoon_minutes

    # FA
    answer = total_minutes
    return answer