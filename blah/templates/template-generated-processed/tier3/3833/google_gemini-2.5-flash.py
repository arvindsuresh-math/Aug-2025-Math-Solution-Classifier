from fractions import Fraction

def solve():
    """Index: 3833.
    Returns: the total number of candles remaining in the room.
    """
    # L1
    total_candles = 40 # jointly bought 40 candles
    alyssa_fraction = Fraction(1, 2) # used half of them
    alyssa_used_candles = alyssa_fraction * total_candles

    # L2
    remaining_candles_after_alyssa = total_candles - alyssa_used_candles

    # L3
    chelsea_percentage = Fraction(70, 100) # 70% of the remaining candles
    chelsea_used_candles = chelsea_percentage * remaining_candles_after_alyssa

    # L4
    candles_remaining_in_room = total_candles - alyssa_used_candles - chelsea_used_candles

    # FA
    answer = candles_remaining_in_room
    return answer