def solve():
    """Index: 5816.
    Returns: the total amount of money Chandler will pay.
    """
    # L1
    num_movie_tickets = 8 # eight movie tickets
    movie_ticket_price = 30 # each movie ticket is sold at $30
    cost_eight_movie_tickets = num_movie_tickets * movie_ticket_price

    # L2
    cost_multiplier = 2 # 2 times as much
    cost_one_football_ticket = cost_eight_movie_tickets / cost_multiplier

    # L3
    num_football_tickets = 5 # five football game tickets
    cost_five_football_tickets = num_football_tickets * cost_one_football_ticket

    # L4
    total_cost = cost_five_football_tickets + cost_eight_movie_tickets

    # FA
    answer = total_cost
    return answer