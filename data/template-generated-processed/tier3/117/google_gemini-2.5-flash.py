def solve():
    """Index: 117.
    Returns: the number of clownfish now in the display tank.
    """
    # L1
    total_fish = 100 # combined total of 100 fish
    equal_parts = 2 # equal number of clownfish and blowfish
    initial_blowfish = total_fish / equal_parts

    # L2
    blowfish_staying_in_own_tank = 26 # 26 of the blowfish stay in their own tank
    blowfish_in_display_tank = initial_blowfish - blowfish_staying_in_own_tank

    # L3
    clownfish_return_divisor = 3 # a third of these clownfish
    clownfish_swam_back = blowfish_in_display_tank / clownfish_return_divisor

    # L4
    clownfish_in_display_tank_final = blowfish_in_display_tank - clownfish_swam_back

    # FA
    answer = clownfish_in_display_tank_final
    return answer