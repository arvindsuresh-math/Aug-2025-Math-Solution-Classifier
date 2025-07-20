from fractions import Fraction

def solve():
    """Index: 5540.
    Returns: the additional kilometers Lucy needs to run to cover the same distance as Mary.
    """
    # L1
    mary_fraction_distance = Fraction(3, 8) # 3/8 of a 24-kilometer field
    total_field_distance = 24 # 24-kilometer field
    mary_distance_ran = mary_fraction_distance * total_field_distance

    # L2
    edna_fraction_of_mary = Fraction(2, 3) # 2/3 of the distance of Edna
    edna_distance_ran = edna_fraction_of_mary * mary_distance_ran

    # L3
    lucy_fraction_of_edna = Fraction(5, 6) # 5/6 of the distance of Edna
    lucy_distance_ran = lucy_fraction_of_edna * edna_distance_ran

    # L4
    kilometers_needed_by_lucy = mary_distance_ran - lucy_distance_ran

    # FA
    answer = kilometers_needed_by_lucy
    return answer