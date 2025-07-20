def solve():
    """Index: 6826.
    Returns: the difference in the number of dolls with black and brown hair combined and blonde-haired dolls.
    """
    # L1
    blonde_hair_dolls = 4 # 4 dolls with blonde hair
    multiplier_brown_blonde = 4 # four times more dolls with brown than blonde hair
    brown_hair_dolls = blonde_hair_dolls * multiplier_brown_blonde

    # L2
    fewer_black_than_brown = 2 # 2 fewer dolls with black than brown hair
    black_hair_dolls = brown_hair_dolls - fewer_black_than_brown

    # L3
    black_brown_combined = brown_hair_dolls + black_hair_dolls

    # L4
    difference_black_brown_blonde = black_brown_combined - blonde_hair_dolls

    # FA
    answer = difference_black_brown_blonde
    return answer