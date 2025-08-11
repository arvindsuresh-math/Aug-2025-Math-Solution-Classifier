def solve():
    """Index: 2223.
    Returns: the number of pieces of gum Shane has left.
    """
    # L1
    total_gum_elyse = 100 # 100 pieces of gum
    half_divisor = 2 # half to her brother Rick
    gum_to_rick = total_gum_elyse / half_divisor

    # L2
    gum_to_shane = gum_to_rick / half_divisor

    # L3
    chewed_gum = 11 # chewed 11 pieces of gum
    shane_gum_left = gum_to_shane - chewed_gum

    # FA
    answer = shane_gum_left
    return answer