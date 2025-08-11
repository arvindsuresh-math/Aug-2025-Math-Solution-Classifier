def solve():
    """Index: 7270.
    Returns: the time it will take Bob to till the plot in minutes.
    """
    # L1
    plot_width = 110 # 110 feet wide
    tiller_swath_width = 2 # two feet wide
    plot_length = 120 # 120 feet long
    num_rows = plot_width / tiller_swath_width

    # L2
    total_feet_tilled = plot_length * num_rows

    # L3
    time_per_foot = 2 # 2 seconds
    total_seconds = time_per_foot * total_feet_tilled

    # L4
    seconds_per_minute = 60 # WK
    total_minutes = total_seconds / seconds_per_minute

    # FA
    answer = total_minutes
    return answer