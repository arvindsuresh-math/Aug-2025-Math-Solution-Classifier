def solve():
    """Index: 1352.
    Returns: the total amount of airflow created by the fan in one week.
    """
    # L1
    minutes_per_day = 10 # 10 minutes each day
    days_per_week = 7 # WK
    total_minutes_worked = minutes_per_day * days_per_week

    # L2
    seconds_per_minute = 60 # WK
    total_seconds_worked = total_minutes_worked * seconds_per_minute

    # L3
    airflow_rate_lps = 10 # 10 liters per second
    total_airflow = total_seconds_worked * airflow_rate_lps

    # FA
    answer = total_airflow
    return answer