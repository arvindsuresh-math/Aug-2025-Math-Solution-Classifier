from fractions import Fraction

def solve():
    """Index: 5183.
    Returns: the length of the rest of Miss Aisha's body.
    """
    # L1
    leg_fraction = Fraction(1, 3) # 1/3 of her total height
    total_height = 60 # 60 inches tall
    leg_length = leg_fraction * total_height

    # L2
    head_fraction = Fraction(1, 4) # 1/4 of her total height
    head_length = head_fraction * total_height

    # L3
    head_and_legs_length = head_length + leg_length

    # L4
    rest_of_body_length = total_height - head_and_legs_length

    # FA
    answer = rest_of_body_length
    return answer