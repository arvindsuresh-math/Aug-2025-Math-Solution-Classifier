def solve():
    """Index: 4568.
    Returns: the original bet amount.
    """
    # L1
    payout_ratio_numerator = 3 # 3:2 if you get a blackjack
    payout_ratio_denominator = 2 # 3:2 if you get a blackjack
    payout_multiplier = payout_ratio_numerator / payout_ratio_denominator

    # L4
    paid_amount = 60 # paid $60
    original_bet_calculated = paid_amount / payout_multiplier

    # L5
    original_bet = original_bet_calculated

    # FA
    answer = original_bet
    return answer