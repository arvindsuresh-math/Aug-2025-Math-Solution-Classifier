from fractions import Fraction

def solve():
    """Index: 1450.
    Returns: the total number of pairs of socks Caroline has.
    """
    # L1
    initial_pairs = 40 # Caroline has 40 pairs of socks
    lost_pairs = 4 # loses 4 pairs of socks
    remaining_after_loss = initial_pairs - lost_pairs

    # L2
    donated_fraction = Fraction(2, 3) # donates two-thirds
    donated_pairs = remaining_after_loss * donated_fraction

    # L3
    remaining_after_donation = remaining_after_loss - donated_pairs

    # L4
    purchased_pairs = 10 # purchases 10 new pairs of socks
    gifted_pairs = 3 # receives 3 new pairs of socks as a gift
    total_final_pairs = remaining_after_donation + purchased_pairs + gifted_pairs

    # FA
    answer = total_final_pairs
    return answer