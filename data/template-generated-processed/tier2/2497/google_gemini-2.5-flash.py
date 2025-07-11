def solve():
    """Index: 2497.
    Returns: the amount Tim kept from the raffle.
    """
    # L1
    total_raffle_win = 100 # $100 raffle
    given_away_percent = 0.2 # 20% to his friend
    amount_given_away = total_raffle_win * given_away_percent

    # L2
    amount_kept = total_raffle_win - amount_given_away

    # FA
    answer = amount_kept
    return answer