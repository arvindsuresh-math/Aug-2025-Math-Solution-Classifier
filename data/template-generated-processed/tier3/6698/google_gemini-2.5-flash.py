def solve():
    """Index: 6698.
    Returns: the number of days it will take to read all unread messages.
    """
    # L1
    messages_read_per_day = 20 # reading 20 messages a day
    new_messages_per_day = 6 # gets 6 new messages a day
    net_messages_cleared_per_day = messages_read_per_day - new_messages_per_day

    # L2
    initial_unread_messages = 98 # 98 unread messages
    days_to_clear_messages = initial_unread_messages / net_messages_cleared_per_day

    # FA
    answer = days_to_clear_messages
    return answer