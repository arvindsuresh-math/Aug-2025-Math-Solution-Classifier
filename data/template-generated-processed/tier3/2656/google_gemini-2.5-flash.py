from fractions import Fraction

def solve():
    """Index: 2656.
    Returns: the total of all the tagged numbers.
    """
    # L1
    w_tag = 200 # W is tagged with the number 200
    half_fraction = Fraction(1, 2) # half the number W is tagged with
    x_tag = half_fraction * w_tag

    # L2
    w_x_total = x_tag + w_tag

    # L3
    y_tag = w_x_total # Y is tagged with the total of X and W's tags
    w_x_y_total = w_x_total + y_tag

    # L4
    z_tag = 400 # Z is tagged with the number 400
    total_tagged_numbers = w_x_y_total + z_tag

    # FA
    answer = total_tagged_numbers
    return answer