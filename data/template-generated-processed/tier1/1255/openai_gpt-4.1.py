def solve():
    """Index: 1255.
    Returns: the number of baseball game tickets the school sold.
    """
    # L1
    fair_tickets = 25 # 25 fair tickets were sold
    multiplier = 2 # two times the number of fair tickets
    two_times_fair = fair_tickets * multiplier

    # L2
    more_than_two_times = 6 # 6 more than two times
    total_tickets_sold = two_times_fair + more_than_two_times

    # FA
    answer = total_tickets_sold
    return answer