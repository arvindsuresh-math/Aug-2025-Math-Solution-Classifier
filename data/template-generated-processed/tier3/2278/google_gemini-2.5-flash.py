def solve():
    """Index: 2278.
    Returns: the total money Johnny makes in a week.
    """
    # L1
    num_60min_dogs = 6 # 6 dogs have 60-minute walks
    dogs_per_walk = 3 # He can walk 3 dogs at once
    hours_for_60min_walks = num_60min_dogs / dogs_per_walk

    # L2
    pay_per_60min_walk = 20 # $20 for a 60-minute walk
    earnings_60min_walks = pay_per_60min_walk * num_60min_dogs

    # L3
    total_daily_work_hours = 4 # works for 4 hours per day
    remaining_hours = total_daily_work_hours - hours_for_60min_walks
    minutes_per_hour = 60 # WK
    remaining_minutes = remaining_hours * minutes_per_hour

    # L4
    duration_30min_walk = 30 # 30-minute walk
    num_dogs_30min_walks = dogs_per_walk * (remaining_minutes / duration_30min_walk)

    # L5
    pay_per_30min_walk = 15 # $15 for a 30-minute walk
    earnings_30min_walks = pay_per_30min_walk * num_dogs_30min_walks

    # L6
    total_daily_earnings = earnings_60min_walks + earnings_30min_walks

    # L7
    work_days_per_week = 5 # works 5 days
    total_weekly_earnings = total_daily_earnings * work_days_per_week

    # FA
    answer = total_weekly_earnings
    return answer