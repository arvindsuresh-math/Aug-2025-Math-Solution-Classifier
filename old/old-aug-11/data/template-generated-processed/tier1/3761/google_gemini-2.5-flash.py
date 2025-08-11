def solve():
    """Index: 3761.
    Returns: the difference in the number of fleas before and after treatments.
    """
    # L1
    fleas_after_four_treatments = 14 # dog has 14 fleas left
    multiplier_for_half = 2 # One flea treatment gets rid of half the fleas
    fleas_after_three_treatments = fleas_after_four_treatments * multiplier_for_half

    # L2
    fleas_after_two_treatments = fleas_after_three_treatments * multiplier_for_half

    # L3
    fleas_after_one_treatment = fleas_after_two_treatments * multiplier_for_half

    # L4
    fleas_before_treatments = fleas_after_one_treatment * multiplier_for_half

    # L5
    difference_in_fleas = fleas_before_treatments - fleas_after_four_treatments

    # FA
    answer = difference_in_fleas
    return answer