def solve():
    """Index: 2981.
    Returns: the total difference in miles walked by Jackie and Jessie over 6 days.
    """
    # L1
    jackie_daily_miles = 2 # Jackie walks 2 miles each day
    jessie_daily_miles = 1.5 # Jessie walks 1.5 miles each day
    daily_difference = jackie_daily_miles - jessie_daily_miles

    # L2
    num_days = 6 # in 6 days
    total_difference = daily_difference * num_days

    # FA
    answer = total_difference
    return answer