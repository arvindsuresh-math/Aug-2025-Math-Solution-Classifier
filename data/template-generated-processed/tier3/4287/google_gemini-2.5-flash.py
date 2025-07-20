from fractions import Fraction

def solve():
    """Index: 4287.
    Returns: the number of parsley sprigs Carmen has left.
    """
    # L1
    plates_one_sprig = 8 # 8 plates
    whole_sprig_amount = 1 # 1 whole parsley sprig
    sprigs_for_whole_plates = plates_one_sprig * whole_sprig_amount

    # L2
    plates_half_sprig = 12 # 12 plates
    half_sprig_amount = Fraction(1, 2) # 1/2 a sprig
    sprigs_for_half_plates = plates_half_sprig * half_sprig_amount

    # L3
    initial_sprigs = 25 # started with 25 parsley sprigs
    total_sprigs_used = sprigs_for_whole_plates + sprigs_for_half_plates

    # L4
    sprigs_left = initial_sprigs - total_sprigs_used

    # FA
    answer = sprigs_left
    return answer