def solve():
    """Index: 3520.
    Returns: the percentage of total time spent watching the comet, rounded to the nearest percent.
    """
    # L1
    shopping_hours = 2 # two hours shopping
    minutes_per_hour = 60 # WK
    shopping_minutes = shopping_hours * minutes_per_hour

    # L2
    setup_hours = 0.5 # half an hour getting everything set up
    setup_minutes = setup_hours * minutes_per_hour

    # L3
    snack_time_multiplier = 3 # three times the setup time
    snack_minutes = snack_time_multiplier * setup_minutes

    # L4
    total_time_minutes = shopping_minutes + setup_minutes + snack_minutes

    # L5
    comet_watching_minutes_q = 20 # 20 minutes watching the comet
    percent_multiplier = 100 # WK
    intermediate_percentage_value = (comet_watching_minutes_q / total_time_minutes) * percent_multiplier
    final_percentage = round(intermediate_percentage_value)

    # FA
    answer = final_percentage
    return answer