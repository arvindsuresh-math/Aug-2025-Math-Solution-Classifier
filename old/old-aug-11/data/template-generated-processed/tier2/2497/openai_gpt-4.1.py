def solve():
    """Index: 2497.
    Returns: the amount Tim kept from the $100 raffle after giving away 20% to his friend.
    """
    # L1
    raffle_prize = 100 # Tim won a $100 raffle
    percent_given = 0.2 # gave away 20% to his friend
    amount_given = raffle_prize * percent_given

    # L2
    amount_kept = raffle_prize - amount_given

    # FA
    answer = amount_kept
    return answer