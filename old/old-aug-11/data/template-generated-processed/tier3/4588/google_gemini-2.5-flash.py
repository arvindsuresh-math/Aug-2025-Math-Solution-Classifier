def solve():
    """Index: 4588.
    Returns: the total number of new emails received during the vacation.
    """
    # L1
    initial_emails_day1 = 16 # receives 16 new emails
    half_divisor = 2 # half as many new emails as he received on the prior day
    emails_day2 = initial_emails_day1 / half_divisor

    # L2
    emails_day3 = emails_day2 / half_divisor

    # L3
    emails_day4 = emails_day3 / half_divisor

    # L4
    total_emails = initial_emails_day1 + emails_day2 + emails_day3 + emails_day4

    # FA
    answer = total_emails
    return answer