def solve():
    """Index: 7408.
    Returns: the average rainfall total for the duration of the storm.
    """
    # L1
    initial_rainfall = 5 # 5 inches of rain in the first thirty minutes
    half_divisor = 2 # half that amount
    second_period_rainfall = initial_rainfall / half_divisor

    # L2
    third_period_rainfall_per_hour = 0.5 # 1/2 inch of rain
    third_period_duration_hours = 1 # for the next hour
    third_period_rainfall = third_period_duration_hours * third_period_rainfall_per_hour

    # L3
    total_rainfall = initial_rainfall + second_period_rainfall + third_period_rainfall

    # L4
    first_duration_minutes = 30 # first thirty minutes
    second_duration_minutes = 30 # In the next 30 minutes
    minutes_per_hour = 60 # WK
    total_duration_hours = (first_duration_minutes / minutes_per_hour) + (second_duration_minutes / minutes_per_hour) + third_period_duration_hours
    average_rainfall = total_rainfall / total_duration_hours

    # FA
    answer = average_rainfall
    return answer