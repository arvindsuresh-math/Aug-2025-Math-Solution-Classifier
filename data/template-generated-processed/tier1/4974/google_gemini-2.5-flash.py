def solve():
    """Index: 4974.
    Returns: the total amount John makes a week.
    """
    # L1
    days_in_week = 7 # WK
    days_off_streaming = 3 # 3 days off of streaming per week
    streaming_days_per_week = days_in_week - days_off_streaming

    # L2
    hours_per_stream_day = 4 # streams for 4 hours at a time
    total_streaming_hours_per_week = streaming_days_per_week * hours_per_stream_day

    # L3
    hourly_rate = 10 # makes $10 an hour
    weekly_earnings = total_streaming_hours_per_week * hourly_rate

    # FA
    answer = weekly_earnings
    return answer