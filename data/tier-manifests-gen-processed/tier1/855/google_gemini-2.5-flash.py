def solve():
    """Index: 855.
    Returns: the initial amount of money Noemi had.
    """
    # L1
    lost_on_roulette = 400 # lost $400 on roulette
    lost_on_blackjack = 500 # lost $500 on blackjack
    total_lost_money = lost_on_roulette + lost_on_blackjack

    # L2
    remaining_money = 800 # still had $800 in her purse
    initial_money = total_lost_money + remaining_money

    # FA
    answer = initial_money
    return answer