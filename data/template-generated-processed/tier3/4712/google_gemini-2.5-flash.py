def solve():
    """Index: 4712.
    Returns: the total number of hours Tony spends exercising each week.
    """
    # L1
    walk_distance = 3 # walking 3 miles
    walk_speed = 3 # walks at a speed of 3 miles per hour
    walk_time = walk_distance / walk_speed

    # L2
    run_distance = 10 # runs another 10 miles
    run_speed = 5 # runs at a speed of 5 miles per hour
    run_time = run_distance / run_speed

    # L3
    daily_exercise_hours = walk_time + run_time

    # L4
    days_per_week = 7 # one week
    weekly_exercise_hours = daily_exercise_hours * days_per_week

    # FA
    answer = weekly_exercise_hours
    return answer