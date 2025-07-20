def solve():
    """Index: 6861.
    Returns: the total number of ice creams needed to be sold.
    """
    # L1
    game_cost = 60 # The game costs $60
    number_of_players = 2 # for both to be able to afford to buy the game
    total_money_needed = game_cost * number_of_players

    # L2
    ice_cream_price = 5 # sell each ice cream for $5
    number_of_ice_creams = total_money_needed / ice_cream_price

    # FA
    answer = number_of_ice_creams
    return answer