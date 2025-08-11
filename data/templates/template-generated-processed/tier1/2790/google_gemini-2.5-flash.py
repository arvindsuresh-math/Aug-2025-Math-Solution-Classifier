def solve():
    """Index: 2790.
    Returns: the total pounds of bamboo the 9 pandas eat in a week.
    """
    # L1
    num_small_pandas = 4 # Four small panda bears
    bamboo_per_small_panda = 25 # 25 pounds
    total_bamboo_small_pandas_daily = num_small_pandas * bamboo_per_small_panda

    # L2
    num_bigger_pandas = 5 # five bigger panda bears
    bamboo_per_bigger_panda = 40 # 40 pounds
    total_bamboo_bigger_pandas_daily = num_bigger_pandas * bamboo_per_bigger_panda

    # L3
    total_bamboo_all_pandas_daily = total_bamboo_small_pandas_daily + total_bamboo_bigger_pandas_daily

    # L4
    days_in_week = 7 # WK
    total_bamboo_weekly = total_bamboo_all_pandas_daily * days_in_week

    # FA
    answer = total_bamboo_weekly
    return answer