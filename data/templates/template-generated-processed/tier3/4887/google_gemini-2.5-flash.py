from fractions import Fraction

def solve():
    """Index: 4887.
    Returns: the number of stickers Oliver kept.
    """
    # L1
    total_stickers = 135 # Oliver had 135 stickers
    used_fraction = Fraction(1, 3) # used 1/3 of his stickers
    stickers_used = used_fraction * total_stickers

    # L2
    remaining_after_use = total_stickers - stickers_used

    # L3
    friend_fraction = Fraction(2, 5) # gave 2/5 of the remaining to his friend
    stickers_given_to_friend = friend_fraction * remaining_after_use

    # L4
    stickers_kept = remaining_after_use - stickers_given_to_friend

    # FA
    answer = stickers_kept
    return answer