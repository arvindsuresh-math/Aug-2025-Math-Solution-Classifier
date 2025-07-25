def solve():
    """Index: 2148.
    Returns: the total time Missy spends watching TV.
    """
    # L1
    num_reality_shows = 5 # 5 28-minute reality shows
    duration_reality_show = 28 # 28-minute reality shows
    total_reality_show_time = num_reality_shows * duration_reality_show

    # L2
    duration_cartoon = 10 # one 10-minute cartoon
    total_tv_time = total_reality_show_time + duration_cartoon

    # FA
    answer = total_tv_time
    return answer