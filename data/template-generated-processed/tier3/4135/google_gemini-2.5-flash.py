from fractions import Fraction

def solve():
    """Index: 4135.
    Returns: the total number of teeth removed at the dental clinic.
    """
    # L1
    initial_teeth_per_person = 32 # 32 teeth
    first_person_fraction = Fraction(1, 4) # 1/4 of all his teeth removed
    first_person_removed_teeth = first_person_fraction * initial_teeth_per_person

    # L2
    second_person_fraction = Fraction(3, 8) # 3/8 of his teeth removed
    second_person_removed_teeth = second_person_fraction * initial_teeth_per_person

    # L3
    first_and_second_total_removed = second_person_removed_teeth + first_person_removed_teeth

    # L4
    third_person_denominator = 2 # half of his teeth removed
    third_person_removed_teeth = initial_teeth_per_person / third_person_denominator

    # L5
    first_three_total_removed = first_and_second_total_removed + third_person_removed_teeth

    # L6
    last_person_removed_teeth = 4 # the last person only had 4 teeth removed
    total_teeth_removed = first_three_total_removed + last_person_removed_teeth

    # FA
    answer = total_teeth_removed
    return answer