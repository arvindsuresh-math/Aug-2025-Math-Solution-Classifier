def solve():
    """Index: 855.
    Returns: the amount of money Noemi began with.
    """
    # L1
    lost_roulette = 400 # lost $400 on roulette
    lost_blackjack = 500 # lost $500 on blackjack
    total_lost = lost_roulette + lost_blackjack

    # L2
    remaining = 800 # she still had $800 in her purse
    initial_money = total_lost + remaining

    # FA
    answer = initial_money
    return answer