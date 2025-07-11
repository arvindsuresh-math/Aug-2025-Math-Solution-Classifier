def solve():
    """Index: 2874.
    Returns: the average number of text messages sent per day.
    """
    # L1
    messages_monday = 220 # 220 text messages on Monday
    tuesday_divisor = 2 # half as many text messages on Tuesday
    messages_tuesday = messages_monday / tuesday_divisor

    # L2
    messages_wed_fri_per_day = 50 # 50 text messages each day Wednesday through Friday
    num_days_wed_fri = 3 # WK
    messages_wed_fri_total = messages_wed_fri_per_day * num_days_wed_fri

    # L3
    total_messages = messages_tuesday + messages_wed_fri_total + messages_monday

    # L4
    total_days = 5 # WK
    average_messages_per_day = total_messages / total_days

    # FA
    answer = average_messages_per_day
    return answer