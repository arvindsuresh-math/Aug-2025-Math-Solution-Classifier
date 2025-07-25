def solve():
    """Index: 293.
    Returns: the total combined amount of time Carlotta spends practicing, throwing tantrums, and singing.
    """
    # L1
    stage_performance_minutes = 6 # final stage performance is 6 minutes long
    practice_per_minute_singing = 3 # an additional 3 minutes practicing
    total_practice_time = stage_performance_minutes * practice_per_minute_singing

    # L2
    tantrum_per_minute_singing = 5 # 5 minutes throwing temper tantrums
    total_tantrum_time = stage_performance_minutes * tantrum_per_minute_singing

    # L3
    total_combined_time = total_practice_time + total_tantrum_time + stage_performance_minutes

    # FA
    answer = total_combined_time
    return answer