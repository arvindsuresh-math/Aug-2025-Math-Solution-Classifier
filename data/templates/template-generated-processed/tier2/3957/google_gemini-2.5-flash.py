def solve():
    """Index: 3957.
    Returns: the total money Joanne makes in 5 days.
    """
    # L1
    main_job_hours_per_day = 8 # 8 hours a day
    main_job_hourly_rate = 16.00 # $16.00 working at her main job
    main_job_daily_earnings = main_job_hours_per_day * main_job_hourly_rate

    # L2
    work_days_per_week = 5 # 5 days a week
    main_job_weekly_earnings = main_job_daily_earnings * work_days_per_week

    # L3
    part_time_job_hours_per_day = 2 # working an extra 2 hours a day
    part_time_job_hourly_rate = 13.50 # makes $13.50 an hour
    part_time_job_daily_earnings = part_time_job_hours_per_day * part_time_job_hourly_rate

    # L4
    part_time_job_weekly_earnings = part_time_job_daily_earnings * work_days_per_week

    # L5
    total_weekly_earnings = main_job_weekly_earnings + part_time_job_weekly_earnings

    # FA
    answer = total_weekly_earnings
    return answer