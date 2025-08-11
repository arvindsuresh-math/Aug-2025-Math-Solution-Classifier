from fractions import Fraction

def solve():
    """Index: 5848.
    Returns: the total number of oranges in both boxes.
    """
    # L1
    capacity_box1 = 80 # capacity of 80
    fill_fraction_box1 = Fraction(3, 4) # 3/4 full
    oranges_box1 = fill_fraction_box1 * capacity_box1

    # L2
    capacity_box2 = 50 # capacity of 50
    fill_fraction_box2 = Fraction(3, 5) # 3/5 full
    oranges_box2 = fill_fraction_box2 * capacity_box2

    # L3
    total_oranges = oranges_box1 + oranges_box2

    # FA
    answer = total_oranges
    return answer