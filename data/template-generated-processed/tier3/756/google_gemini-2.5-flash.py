from fractions import Fraction

def solve():
    """Index: 756.
    Returns: the total number of stamps Anna had in the end.
    """
    # L1
    fraction_given = Fraction(1, 2) # half of her collection
    alison_stamps = 28 # Alison had 28 stamps
    stamps_from_alison = fraction_given * alison_stamps

    # L2
    anna_initial_stamps = 37 # Anna had 37 stamps in her collection
    anna_stamps_after_alison = stamps_from_alison + anna_initial_stamps

    # L3
    stamps_traded_away = 2 # traded Jeff two bluebird stamps
    anna_stamps_after_trade_away = anna_stamps_after_alison - stamps_traded_away

    # L4
    stamps_received_back = 1 # for one mountain stamp
    anna_final_stamps = anna_stamps_after_trade_away + stamps_received_back

    # FA
    answer = anna_final_stamps
    return answer