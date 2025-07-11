def solve():
    """Index: 117.
    Returns: the number of clownfish now in the display tank.
    """
    # L1
    total_fish = 100 # aquarium holds a combined total of 100 fish
    fish_types = 2 # equal number of clownfish and blowfish
    blowfish = total_fish / fish_types

    # L2
    blowfish_stay = 26 # 26 of the blowfish stay in their own tank
    blowfish_display = blowfish - blowfish_stay

    # L3
    clownfish_joining = blowfish_display # equal number of clownfish join the blowfish in the display tank
    clownfish_swim_back_divisor = 3 # a third of these clownfish swim back
    clownfish_swim_back = clownfish_joining / clownfish_swim_back_divisor

    # L4
    clownfish_display = clownfish_joining - clownfish_swim_back

    # FA
    answer = clownfish_display
    return answer