def solve():
    """Index: 4635.
    Returns: the total number of red colored pencils Johnny bought.
    """
    # L1
    num_packs = 15 # 15 packs of colored pencils
    red_pencils_per_normal_pack = 1 # a red, yellow, and green pencil inside
    red_pencils_from_normal_packs = num_packs * red_pencils_per_normal_pack

    # L2
    packs_with_extra = 3 # 3 of the packs
    extra_red_per_pack = 2 # two extra red pencils
    extra_red_pencils_total = packs_with_extra * extra_red_per_pack

    # L3
    total_red_pencils = red_pencils_from_normal_packs + extra_red_pencils_total

    # FA
    answer = total_red_pencils
    return answer