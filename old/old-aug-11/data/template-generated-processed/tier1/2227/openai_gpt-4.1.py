def solve():
    """Index: 2227.
    Returns: the total number of tickets Russel and Jen used at the circus.
    """
    # L1
    shooting_game_cost = 5 # shooting game costs 5 tickets
    jen_plays = 2 # Jen played a shooting game twice
    jen_tickets = shooting_game_cost * jen_plays

    # L2
    carousel_cost = 3 # carousel costs 3 tickets
    russel_rides = 3 # Russel rode the carousel three times
    russel_tickets = carousel_cost * russel_rides

    # L3
    total_tickets = jen_tickets + russel_tickets

    # FA
    answer = total_tickets
    return answer