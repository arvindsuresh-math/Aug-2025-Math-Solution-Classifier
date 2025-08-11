def solve():
    """Index: 1709.
    Returns: the total number of messages sent in the Whatsapp group after four days.
    """
    # L1
    monday_messages = 300 # 300 messages were sent by the members on Monday
    tuesday_messages = 200 # 200 messages on Tuesday
    mon_tue_total = monday_messages + tuesday_messages

    # L2
    wednesday_more_than_prev = 300 # 300 more messages on Wednesday than the previous day
    wednesday_messages = wednesday_more_than_prev + tuesday_messages

    # L3
    three_day_total = mon_tue_total + wednesday_messages

    # L4
    thursday_multiplier = 2 # two times as many messages on Thursday as there were on Wednesday
    thursday_messages = thursday_multiplier * wednesday_messages

    # L5
    four_day_total = three_day_total + thursday_messages

    # FA
    answer = four_day_total
    return answer