def solve():
    """Index: 932.
    Returns: the number of client requests Maia will have remaining after 5 days.
    """
    # L1
    requests_per_day = 6 # gets 6 client requests every day
    works_on_per_day = 4 # works on four of them each day
    remaining_per_day = requests_per_day - works_on_per_day

    # L2
    num_days = 5 # after 5 days
    total_remaining = num_days * remaining_per_day

    # FA
    answer = total_remaining
    return answer