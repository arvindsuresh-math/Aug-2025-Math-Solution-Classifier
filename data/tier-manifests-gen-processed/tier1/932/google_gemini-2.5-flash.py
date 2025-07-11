def solve():
    """Index: 932.
    Returns: the number of client requests remaining to work on after 5 days.
    """
    # L1
    client_requests_daily = 6 # 6 client requests every day
    worked_on_daily = 4 # works on four of them each day
    remaining_daily = client_requests_daily - worked_on_daily

    # L2
    num_days = 5 # after 5 days
    total_remaining = num_days * remaining_daily

    # FA
    answer = total_remaining
    return answer