def solve():
    """Index: 3150.
    Returns: the number of games Percy needs to sell.
    """
    # L1
    playstation_cost = 500 # PlayStation, which costs $500
    birthday_money = 200 # $200 on his birthday
    christmas_money = 150 # $150 at Christmas
    money_needed = playstation_cost - birthday_money - christmas_money

    # L2
    game_price = 7.5 # $7.5 each
    games_to_sell = money_needed / game_price

    # FA
    answer = games_to_sell
    return answer