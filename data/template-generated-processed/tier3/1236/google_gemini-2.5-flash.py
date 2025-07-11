from fractions import Fraction

def solve():
    """Index: 1236.
    Returns: the number of grey cats in the house.
    """
    # L1
    total_cats = 16 # 16 cats
    black_percentage = Fraction(25, 100) # 25% of them are black
    black_cats = total_cats * black_percentage

    # L2
    white_cats = 2 # Two of them are white
    grey_cats = total_cats - black_cats - white_cats

    # FA
    answer = grey_cats
    return answer