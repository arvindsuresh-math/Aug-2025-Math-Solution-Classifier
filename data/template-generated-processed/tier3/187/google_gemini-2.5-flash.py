from fractions import Fraction

def solve():
    """Index: 187.
    Returns: the total number of unused crayons Madeline has.
    """
    # L1
    crayons_per_box = 24 # 24 crayons in each
    unused_fraction_first_two_boxes = Fraction(5, 8) # 5/8 of the crayons
    unused_crayons_per_box_first_two = crayons_per_box * unused_fraction_first_two_boxes

    # L2
    num_boxes_first_set = 2 # the 2 boxes
    total_unused_crayons_first_two_boxes = unused_crayons_per_box_first_two * num_boxes_first_set

    # L3
    used_fraction_other_two_boxes = Fraction(2, 3) # 2/3 of the crayons were used
    used_crayons_per_box_other_two = crayons_per_box * used_fraction_other_two_boxes

    # L4
    unused_crayons_per_box_other_two = crayons_per_box - used_crayons_per_box_other_two

    # L5
    num_boxes_other_set = 2 # 2 other boxes
    total_unused_crayons_other_two_boxes = unused_crayons_per_box_other_two * num_boxes_other_set

    # L6
    unused_crayons_last_box = 24 # the last box was not entirely used
    total_unused_crayons = total_unused_crayons_first_two_boxes + total_unused_crayons_other_two_boxes + unused_crayons_last_box

    # FA
    answer = total_unused_crayons
    return answer