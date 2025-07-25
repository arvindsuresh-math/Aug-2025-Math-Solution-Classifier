from fractions import Fraction

def solve():
    """Index: 3949.
    Returns: the number of Japanese stamps Nikka has.
    """
    # L1
    total_stamps = 100 # 100 stamp collection
    chinese_percentage = Fraction(35, 100) # Thirty-five percent of her stamps are Chinese
    chinese_stamps = total_stamps * chinese_percentage

    # L2
    us_percentage = Fraction(20, 100) # 20% are US stamps
    us_stamps = total_stamps * us_percentage

    # L3
    non_japanese_stamps = chinese_stamps + us_stamps

    # L4
    japanese_stamps = total_stamps - non_japanese_stamps

    # FA
    answer = japanese_stamps
    return answer