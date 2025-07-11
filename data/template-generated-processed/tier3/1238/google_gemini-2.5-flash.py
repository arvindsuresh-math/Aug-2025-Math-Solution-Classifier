from fractions import Fraction

def solve():
    """Index: 1238.
    Returns: the total amount of cereal in all 3 boxes.
    """
    # L1
    first_box_ounces = 14 # One box holds 14 ounces of cereal

    # L2
    half_fraction = Fraction(1, 2) # half the amount
    second_box_ounces = half_fraction * first_box_ounces

    # L3
    less_than_third_box = 5 # 5 ounces less than the third box
    third_box_ounces = second_box_ounces + less_than_third_box

    # L4
    total_cereal_ounces = first_box_ounces + second_box_ounces + third_box_ounces

    # FA
    answer = total_cereal_ounces
    return answer