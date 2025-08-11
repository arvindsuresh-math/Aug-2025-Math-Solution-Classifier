def solve():
    """Index: 2981.
    Returns: how many more miles in all Jackie walks than Jessie in 6 days.
    """
    # L1
    jackie_daily = 2 # Jackie walks 2 miles each day
    jessie_daily = 1.5 # Jessie walks 1.5 miles each day
    daily_difference = jackie_daily - jessie_daily

    # L2
    num_days = 6 # in 6 days
    total_difference = daily_difference * num_days

    # FA
    answer = total_difference
    return answer