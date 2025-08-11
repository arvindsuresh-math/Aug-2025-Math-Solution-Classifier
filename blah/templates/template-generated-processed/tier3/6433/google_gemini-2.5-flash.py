def solve():
    """Index: 6433.
    Returns: the number of crayons left in the box.
    """
    # L1
    total_crayons = 48 # 48 crayons in the box
    kiley_fraction_denominator = 4 # 1/4 of them away
    crayons_kiley_takes = total_crayons / kiley_fraction_denominator

    # L2
    remaining_crayons_after_kiley = total_crayons - crayons_kiley_takes

    # L3
    joe_fraction_denominator = 2 # half of the remaining crayons
    crayons_joe_takes = remaining_crayons_after_kiley / joe_fraction_denominator

    # L4
    final_crayons_left = remaining_crayons_after_kiley - crayons_joe_takes

    # FA
    answer = final_crayons_left
    return answer