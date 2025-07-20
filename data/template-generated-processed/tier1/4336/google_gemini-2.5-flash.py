def solve():
    """Index: 4336.
    Returns: the difference in calories burnt if Jonah ran for five hours instead of two.
    """
    # L1
    initial_run_hours = 2 # Running for 2 hours
    calories_per_hour = 30 # burnt 30 calories every hour
    initial_calories_burnt = initial_run_hours * calories_per_hour

    # L2
    target_run_hours = 5 # run for five hours
    target_calories_burnt = target_run_hours * calories_per_hour

    # L3
    calorie_difference = target_calories_burnt - initial_calories_burnt

    # FA
    answer = calorie_difference
    return answer