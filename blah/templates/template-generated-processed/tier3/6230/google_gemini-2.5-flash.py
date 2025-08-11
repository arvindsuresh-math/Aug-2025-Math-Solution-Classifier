from fractions import Fraction

def solve():
    """Index: 6230.
    Returns: the number of apple slices Tom has left.
    """
    # L1
    num_apples = 2 # 2 apples
    slices_per_apple = 8 # 8 slices each
    total_slices = num_apples * slices_per_apple

    # L2
    fraction_given_to_jerry = Fraction(3, 8) # 3/8ths of the apple slices
    slices_given_to_jerry = total_slices * fraction_given_to_jerry

    # L3
    remaining_slices_after_jerry = total_slices - slices_given_to_jerry

    # L4
    half_divisor = 2 # half of the remaining slices
    final_slices_left = remaining_slices_after_jerry / half_divisor

    # FA
    answer = final_slices_left
    return answer