from fractions import Fraction

def solve():
    """Index: 187.
    Returns: the total number of unused crayons Madeline has.
    """
    # L1
    crayons_per_box = 24 # 24 crayons in each
    unused_fraction_first_two = Fraction(5, 8) # 5/8 of the crayons in the 2 boxes were not yet used
    unused_crayons_per_first_box = crayons_per_box * unused_fraction_first_two

    # L2
    first_two_boxes = 2 # 2 boxes
    total_unused_first_two = unused_crayons_per_first_box * first_two_boxes

    # L3
    used_fraction_next_two = Fraction(2, 3) # 2/3 of the crayons were used
    used_crayons_per_next_box = crayons_per_box * used_fraction_next_two

    # L4
    unused_crayons_per_next_box = crayons_per_box - used_crayons_per_next_box

    # L5
    next_two_boxes = 2 # 2 other boxes
    total_unused_next_two = unused_crayons_per_next_box * next_two_boxes

    # L6
    last_box_unused = crayons_per_box # last box was not entirely used (implies all unused)
    total_unused = total_unused_first_two + total_unused_next_two + last_box_unused

    # FA
    answer = total_unused
    return answer