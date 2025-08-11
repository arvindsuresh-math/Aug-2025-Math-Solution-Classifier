def solve():
    """Index: 546.
    Returns: the total number of gifts received between two birthdays.
    """
    # L1
    gifts_12th_birthday = 20 # 20 gifts on his 12th birthday
    fewer_gifts_13th = 8 # 8 fewer gifts on his 13th birthday
    gifts_13th_birthday = gifts_12th_birthday - fewer_gifts_13th

    # L2
    total_gifts = gifts_12th_birthday + gifts_13th_birthday

    # FA
    answer = total_gifts
    return answer