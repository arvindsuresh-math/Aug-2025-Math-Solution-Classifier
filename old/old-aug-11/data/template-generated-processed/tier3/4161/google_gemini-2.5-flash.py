from fractions import Fraction

def solve():
    """Index: 4161.
    Returns: the number of flowers remaining in the garden.
    """
    # L1
    num_rows = 50 # 50 rows
    flowers_per_row = 400 # 400 flowers
    total_flowers_initial = num_rows * flowers_per_row

    # L2
    cut_percentage = Fraction(60, 100) # 60% of the flowers
    flowers_cut = cut_percentage * total_flowers_initial

    # L3
    flowers_remaining = total_flowers_initial - flowers_cut

    # FA
    answer = flowers_remaining
    return answer