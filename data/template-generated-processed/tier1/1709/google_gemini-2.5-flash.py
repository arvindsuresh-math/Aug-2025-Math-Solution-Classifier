def solve():
    """Index: 1709.
    Returns: the total number of messages sent in the Whatsapp group after the four days.
    """
    # L1
    messages_monday = 300 # 300 messages were sent by the members on Monday
    messages_tuesday = 200 # 200 messages on Tuesday
    messages_mon_tue_sum = messages_monday + messages_tuesday

    # L2
    wednesday_increase = 300 # 300 more messages on Wednesday than the previous day
    messages_wednesday = wednesday_increase + messages_tuesday

    # L3
    messages_three_days = messages_mon_tue_sum + messages_wednesday

    # L4
    thursday_multiplier = 2 # two times as many messages on Thursday
    messages_thursday = thursday_multiplier * messages_wednesday

    # L5
    total_messages_four_days = messages_three_days + messages_thursday

    # FA
    answer = total_messages_four_days
    return answer