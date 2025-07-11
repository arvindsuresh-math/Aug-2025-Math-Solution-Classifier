def solve():
    """Index: 327.
    Returns: the number of coats Andy can make.
    """
    # L1
    initial_minks = 30 # Andy buys 30 minks
    babies_per_mink = 6 # each mink has 6 babies
    total_baby_minks = initial_minks * babies_per_mink

    # L2
    total_minks_before_release = total_baby_minks + initial_minks

    # L3
    release_divisor = 2 # half the total minks are set free
    remaining_minks = total_minks_before_release / release_divisor

    # L4
    minks_per_coat = 15 # It takes 15 mink skins to make a coat
    num_coats = remaining_minks / minks_per_coat

    # FA
    answer = num_coats
    return answer