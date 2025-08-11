def solve():
    """Index: 3103.
    Returns: the number of tickets Taegan won from each game.
    """
    # L1
    total_value_of_tickets = 30 # tickets that total a value of $30
    value_per_ticket = 3 # Each ticket is worth $3
    total_tickets_won = total_value_of_tickets / value_per_ticket

    # L2
    found_tickets = 5 # finds 5 tickets on the floor
    tickets_from_games = total_tickets_won - found_tickets

    # L3
    number_of_games = 5 # 5 carnival games
    tickets_per_game = tickets_from_games / number_of_games

    # FA
    answer = tickets_per_game
    return answer