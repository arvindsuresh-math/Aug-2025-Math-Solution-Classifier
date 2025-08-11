def solve():
    """Index: 5404.
    Returns: the total number of pieces of mail Lauren sent.
    """
    # L1
    mail_monday = 65 # 65 pieces of mail on Monday
    more_on_tuesday = 10 # 10 more pieces of mail on Tuesday than on Monday
    mail_tuesday = mail_monday + more_on_tuesday

    # L2
    fewer_on_wednesday = 5 # 5 fewer on Wednesday than on Tuesday
    mail_wednesday = mail_tuesday - fewer_on_wednesday

    # L3
    more_on_thursday = 15 # 15 more pieces of mail on Thursday than on Wednesday
    mail_thursday = mail_wednesday + more_on_thursday

    # L4
    total_mail = mail_monday + mail_tuesday + mail_wednesday + mail_thursday

    # FA
    answer = total_mail
    return answer