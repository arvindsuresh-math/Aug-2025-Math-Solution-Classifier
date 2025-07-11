def solve():
    """Index: 546.
    Returns: the total number of gifts John received on his 12th and 13th birthdays.
    """
    # L1
    gifts_12th = 20 # John received 20 gifts on his 12th birthday
    fewer_gifts_13th = 8 # He received 8 fewer gifts on his 13th birthday
    gifts_13th = gifts_12th - fewer_gifts_13th

    # L2
    total_gifts = gifts_12th + gifts_13th

    # FA
    answer = total_gifts
    return answer