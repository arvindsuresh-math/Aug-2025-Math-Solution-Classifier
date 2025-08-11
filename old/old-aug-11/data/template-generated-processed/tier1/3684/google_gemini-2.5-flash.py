def solve():
    """Index: 3684.
    Returns: the total time in minutes to wash and dry all three loads of laundry.
    """
    # L1
    whites_wash_time = 72 # 72 minutes in the washing machine
    whites_dry_time = 50 # 50 minutes in the dryer
    total_time_whites = whites_wash_time + whites_dry_time

    # L2
    darks_wash_time = 58 # 58 minutes in the washing machine
    darks_dry_time = 65 # 65 minutes in the dryer
    total_time_darks = darks_wash_time + darks_dry_time

    # L3
    colors_wash_time = 45 # 45 minutes in the washer
    colors_dry_time = 54 # 54 minutes in the dryer
    total_time_colors = colors_wash_time + colors_dry_time

    # L4
    total_laundry_time = total_time_whites + total_time_darks + total_time_colors

    # FA
    answer = total_laundry_time
    return answer