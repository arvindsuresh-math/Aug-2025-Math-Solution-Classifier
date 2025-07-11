def solve():
    """Index: 1260.
    Returns: the total amount Jackson spent on entertainment.
    """
    # L1
    num_tickets = 3 # three movie tickets
    cost_per_ticket = 12 # $12 each
    total_movie_cost = num_tickets * cost_per_ticket

    # L2
    computer_game_cost = 66 # computer game for $66
    total_entertainment_cost = total_movie_cost + computer_game_cost

    # FA
    answer = total_entertainment_cost
    return answer