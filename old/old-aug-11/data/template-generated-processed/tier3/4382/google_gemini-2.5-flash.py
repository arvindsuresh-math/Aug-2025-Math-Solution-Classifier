from fractions import Fraction

def solve():
    """Index: 4382.
    Returns: the total number of pink roses in Mrs. Dawson's rose garden.
    """
    # L1
    roses_per_row = 20 # 20 roses
    red_fraction = Fraction(1, 2) # 1/2 of these roses are red
    red_roses_per_row = roses_per_row * red_fraction

    # L2
    remaining_roses_after_red = roses_per_row - red_roses_per_row

    # L3
    white_fraction = Fraction(3, 5) # 3/5 of the remaining are white
    white_roses_per_row = remaining_roses_after_red * white_fraction

    # L4
    pink_roses_per_row = remaining_roses_after_red - white_roses_per_row

    # L5
    num_rows = 10 # 10 rows of roses
    total_pink_roses = pink_roses_per_row * num_rows

    # FA
    answer = total_pink_roses
    return answer