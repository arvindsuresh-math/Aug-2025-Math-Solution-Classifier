def solve():
    """Index: 5166.
    Returns: the number of tickets sold to the horror movie.
    """
    # L1
    romance_tickets = 25 # 25 tickets to the romance movie
    multiplier_three_times = 3 # three times the number of tickets
    three_times_romance = romance_tickets * multiplier_three_times

    # L2
    more_than_three_times = 18 # 18 more than three times
    horror_tickets = three_times_romance + more_than_three_times

    # FA
    answer = horror_tickets
    return answer