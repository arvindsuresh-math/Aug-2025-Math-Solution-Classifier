def solve():
    """Index: 327.
    Returns: the number of coats Andy can make.
    """
    # L1
    adult_minks = 30 # Andy buys 30 minks
    babies_per_mink = 6 # each mink has 6 babies
    total_baby_minks = adult_minks * babies_per_mink

    # L2
    total_minks = total_baby_minks + adult_minks

    # L3
    freed_divisor = 2 # half the total minks are set free
    remaining_minks = total_minks / freed_divisor

    # L4
    minks_per_coat = 15 # 15 mink skins to make a coat
    coats = remaining_minks / minks_per_coat

    # FA
    answer = coats
    return answer