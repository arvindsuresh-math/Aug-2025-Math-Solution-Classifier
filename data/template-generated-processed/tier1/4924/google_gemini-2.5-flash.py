def solve():
    """Index: 4924.
    Returns: the total amount of money Diane lost.
    """
    # L1
    initial_money = 100 # starts with $100
    won_money = 65 # wins 5 hands for a total of $65 dollars
    mid_game_money = initial_money + won_money

    # L2
    owed_money = 50 # owing her friends $50
    total_lost = mid_game_money + owed_money

    # FA
    answer = total_lost
    return answer