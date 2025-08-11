def solve():
    """Index: 2790.
    Returns: the total pounds of bamboo the 9 pandas eat in a week.
    """
    # L1
    num_small_pandas = 4 # Four small panda bears
    small_panda_daily = 25 # 25 pounds ... every day
    small_total_daily = num_small_pandas * small_panda_daily

    # L2
    num_big_pandas = 5 # five bigger panda bears
    big_panda_daily = 40 # 40 pounds ... every day
    big_total_daily = num_big_pandas * big_panda_daily

    # L3
    total_daily = small_total_daily + big_total_daily

    # L4
    days_in_week = 7 # WK
    total_weekly = total_daily * days_in_week

    # FA
    answer = total_weekly
    return answer