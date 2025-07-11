def solve():
    """Index: 1255.
    Returns: the number of baseball game tickets sold.
    """
    # L1
    fair_tickets_sold = 25 # 25 fair tickets were sold
    multiplier_two = 2 # WK
    two_times_fair_tickets = fair_tickets_sold * multiplier_two

    # L2
    more_than_two_times = 6 # 6 more than two times
    baseball_game_tickets = two_times_fair_tickets + more_than_two_times

    # FA
    answer = baseball_game_tickets
    return answer