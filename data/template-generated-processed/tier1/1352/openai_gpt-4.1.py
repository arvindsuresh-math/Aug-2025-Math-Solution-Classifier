def solve():
    """Index: 1352.
    Returns: the total amount of airflow the fan will create in one week (in liters).
    """
    # L1
    minutes_per_day = 10 # fan works for 10 minutes each day
    days_per_week = 7 # WK
    total_minutes = minutes_per_day * days_per_week

    # L2
    seconds_per_minute = 60 # WK
    total_seconds = total_minutes * seconds_per_minute

    # L3
    liters_per_second = 10 # airflow of 10 liters per second
    total_airflow = total_seconds * liters_per_second

    # FA
    answer = total_airflow
    return answer