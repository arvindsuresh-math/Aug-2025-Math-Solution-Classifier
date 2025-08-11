def solve():
    """Index: 5387.
    Returns: the total number of emails Jimmy's father had at the end of April.
    """
    # L1
    days_in_april = 30 # WK
    half_divisor = 2 # WK
    first_half_days = days_in_april / half_divisor

    # L2
    daily_emails_initial = 20 # 20 emails a day
    emails_first_half = daily_emails_initial * first_half_days

    # L3
    additional_emails_per_day = 5 # sent 5 more emails per day
    daily_emails_after_subscription = daily_emails_initial + additional_emails_per_day

    # L4
    emails_second_half = daily_emails_after_subscription * first_half_days

    # L5
    total_emails_april = emails_second_half + emails_first_half

    # FA
    answer = total_emails_april
    return answer