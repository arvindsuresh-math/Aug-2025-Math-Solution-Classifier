from fractions import Fraction

def solve():
    """Index: 2658.
    Returns: the total number of stickers Zander gave to his two friends.
    """
    # L1
    total_stickers = 100 # Zander collected 100 stickers
    andrew_fraction = Fraction(1, 5) # Andrew received 1/5 of Zander's stickers
    andrew_stickers = total_stickers * andrew_fraction

    # L2
    remaining_stickers_after_andrew = total_stickers - andrew_stickers

    # L3
    bill_fraction = Fraction(3, 10) # Bill received 3/10 of the remaining stickers
    bill_stickers = remaining_stickers_after_andrew * bill_fraction

    # L4
    total_given_away = andrew_stickers + bill_stickers

    # FA
    answer = total_given_away
    return answer