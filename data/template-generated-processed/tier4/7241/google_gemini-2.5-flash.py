from fractions import Fraction

def solve():
    """Index: 7241.
    Returns: the amount Claire will earn from selling red roses.
    """
    # L1
    total_flowers = 400 # 400 flowers in her garden
    num_tulips = 120 # One hundred twenty are tulips
    num_roses = total_flowers - num_tulips

    # L2
    num_white_roses = 80 # Eighty of the roses are white
    num_red_roses = num_roses - num_white_roses

    # L3
    fraction_to_sell = Fraction(1, 2) # 1/2 of the total number of red roses
    roses_to_sell = fraction_to_sell * num_red_roses

    # L4
    value_per_red_rose = 0.75 # Each red rose is worth $0.75
    total_earnings = value_per_red_rose * roses_to_sell

    # FA
    answer = total_earnings
    return answer