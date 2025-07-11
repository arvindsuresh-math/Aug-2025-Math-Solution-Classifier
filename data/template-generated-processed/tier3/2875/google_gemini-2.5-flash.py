from fractions import Fraction

def solve():
    """Index: 2875.
    Returns: the total distance Ken will cover.
    """
    # L1
    distance_ken_dawn = 4 # Ken's house is 4 miles away from Dawn's house
    half_factor = Fraction(1, 2) # half that
    distance_ken_mary = half_factor * distance_ken_dawn

    # L2
    leg1_distance = distance_ken_dawn

    # L3
    total_distance_after_mary = leg1_distance + distance_ken_mary

    # L4
    distance_mary_dawn = distance_ken_mary # another 2 miles (implied Mary's to Dawn's is same as Ken's to Mary's)
    total_distance_back_to_dawn = total_distance_after_mary + distance_mary_dawn

    # L5
    distance_dawn_ken = distance_ken_dawn # 4 miles (back to his own house)
    final_total_distance = total_distance_back_to_dawn + distance_dawn_ken

    # FA
    answer = final_total_distance
    return answer