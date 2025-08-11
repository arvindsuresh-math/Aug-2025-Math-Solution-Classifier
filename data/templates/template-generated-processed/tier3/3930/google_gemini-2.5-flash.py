from fractions import Fraction

def solve():
    """Index: 3930.
    Returns: the average time Jonsey and Riley spend inside.
    """
    # L1
    hours_in_day = 24 # WK
    jonsey_awake_fraction = Fraction(2, 3) # 2/3 of the day
    jonsey_awake_hours = hours_in_day * jonsey_awake_fraction

    # L2
    whole_fraction = 1 # WK
    jonsey_outside_fraction = Fraction(1, 2) # 1/2 her time awake playing outside
    jonsey_inside_fraction = whole_fraction - jonsey_outside_fraction

    # L3
    jonsey_inside_hours = jonsey_awake_hours * jonsey_inside_fraction

    # L4
    riley_awake_fraction = Fraction(3, 4) # 3/4 of the day
    riley_awake_hours = hours_in_day * riley_awake_fraction

    # L5
    riley_outside_fraction = Fraction(1, 3) # 1/3 of his day outside
    riley_inside_fraction = whole_fraction - riley_outside_fraction

    # L6
    riley_inside_hours = riley_awake_hours * riley_inside_fraction

    # L7
    total_inside_hours = jonsey_inside_hours + riley_inside_hours

    # L8
    number_of_people = 2 # WK
    average_inside_hours = total_inside_hours / number_of_people

    # FA
    answer = average_inside_hours
    return answer