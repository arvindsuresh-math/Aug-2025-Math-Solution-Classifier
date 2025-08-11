from fractions import Fraction

def solve():
    """Index: 6928.
    Returns: the total number of apples not sold.
    """
    # L1
    num_boxes = 10 # orders 10 boxes of apples
    apples_per_box = 300 # each box has 300 apples
    apples_ordered_weekly = num_boxes * apples_per_box

    # L2
    fraction_sold = Fraction(3, 4) # sells 3/4 of his stock
    apples_sold = fraction_sold * apples_ordered_weekly

    # L3
    apples_not_sold = apples_ordered_weekly - apples_sold

    # FA
    answer = apples_not_sold
    return answer