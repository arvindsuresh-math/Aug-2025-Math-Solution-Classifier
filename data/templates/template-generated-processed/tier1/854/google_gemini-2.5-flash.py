def solve():
    """Index: 854.
    Returns: the total number of minutes Jeff ran for that week.
    """
    # L1
    run_duration_per_day_minutes = 60 # run for an hour a day
    num_days_mon_wed = 3 # Monday to Wednesday are 3 days
    run_mon_wed = run_duration_per_day_minutes * num_days_mon_wed

    # L2
    cut_short_thursday = 20 # cut short his run by 20 minutes
    run_thursday = run_duration_per_day_minutes - cut_short_thursday

    # L3
    jogged_more_friday = 10 # jog 10 minutes more on Friday
    run_friday = run_duration_per_day_minutes + jogged_more_friday

    # L4
    total_run_time = run_mon_wed + run_thursday + run_friday

    # FA
    answer = total_run_time
    return answer