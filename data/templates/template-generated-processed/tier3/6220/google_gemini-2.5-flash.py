from fractions import Fraction

def solve():
    """Index: 6220.
    Returns: the height of the 6th biggest doll.
    """
    # L1
    biggest_doll_height = 243 # The biggest doll is 243 cm tall
    size_ratio = Fraction(2, 3) # each doll is 2/3rd the size
    second_doll_height = biggest_doll_height * size_ratio

    # L2
    third_doll_height = second_doll_height * size_ratio

    # L3
    fourth_doll_height = third_doll_height * size_ratio

    # L4
    fifth_doll_height = fourth_doll_height * size_ratio

    # L5
    sixth_doll_height = fifth_doll_height * size_ratio

    # FA
    answer = sixth_doll_height
    return answer