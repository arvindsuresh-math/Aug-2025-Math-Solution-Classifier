def solve():
    """Index: 2227.
    Returns: the total number of tickets used by Russel and Jen.
    """
    # L1
    shooting_game_cost = 5 # shooting game costs 5 tickets
    jen_plays_times = 2 # Jen played a shooting game twice
    jen_tickets_used = shooting_game_cost * jen_plays_times

    # L2
    carousel_cost = 3 # carousel costs 3 tickets
    russel_rides_times = 3 # Russel rode the carousel three times
    russel_tickets_used = carousel_cost * russel_rides_times

    # L3
    total_tickets_used = jen_tickets_used + russel_tickets_used

    # FA
    answer = total_tickets_used
    return answer