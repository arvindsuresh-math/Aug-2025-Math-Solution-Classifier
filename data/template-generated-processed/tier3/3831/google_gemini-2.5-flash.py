from fractions import Fraction

def solve():
    """Index: 3831.
    Returns: the number of firecrackers Jerry set off.
    """
    # L1
    initial_firecrackers = 48 # Jerry bought 48 firecrackers
    confiscated_firecrackers = 12 # confiscated 12 of them
    remaining_after_confiscation = initial_firecrackers - confiscated_firecrackers

    # L2
    defective_fraction = Fraction(1, 6) # 1/6 of the remaining ones were defective
    defective_firecrackers = remaining_after_confiscation * defective_fraction

    # L3
    good_firecrackers = remaining_after_confiscation - defective_firecrackers

    # L4
    set_off_divisor = 2 # set off half the good firecrackers
    firecrackers_set_off = good_firecrackers / set_off_divisor

    # FA
    answer = firecrackers_set_off
    return answer