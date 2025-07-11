from fractions import Fraction

def solve():
    """Index: 2448.
    Returns: the total liters of water contained within the bottles.
    """
    # L1
    bottle_capacity = 12 # capacity of 12 liters
    fill_fraction = Fraction(3, 4) # filled up to 3/4 of its capacity
    liters_per_bottle = fill_fraction * bottle_capacity

    # L2
    bottles_per_box = 50 # 50 bottles of water
    liters_per_box = bottles_per_box * liters_per_bottle

    # L3
    num_boxes = 10 # 10 boxes
    total_liters = liters_per_box * num_boxes

    # FA
    answer = total_liters
    return answer