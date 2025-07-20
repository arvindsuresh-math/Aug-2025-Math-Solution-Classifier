def solve():
    """Index: 7098.
    Returns: the total number of fleas on the chickens.
    """
    # L1
    gertrude_fleas = 10 # Gertrude the chicken has 10 fleas
    half_divisor = 2 # half that amount
    olive_fleas = gertrude_fleas / half_divisor

    # L2
    maud_multiplier = 5 # 5 times the amount of fleas as Olive
    maud_fleas = maud_multiplier * olive_fleas

    # L3
    total_fleas = gertrude_fleas + maud_fleas + olive_fleas

    # FA
    answer = total_fleas
    return answer