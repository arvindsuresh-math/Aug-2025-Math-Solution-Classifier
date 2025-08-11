def solve():
    """Index: 5727.
    Returns: the total number of daisies.
    """
    # L1
    pink_multiplier = 9 # nine times as many pink daisies as white daisies
    white_daisies = 6 # 6 white daisies
    pink_daisies = pink_multiplier * white_daisies

    # L2
    red_multiplier = 4 # four times as many red daisies as pink daisies
    temp_red_daisies_multiplied = pink_daisies * red_multiplier

    # L3
    red_less_than = 3 # three less than four times as many red daisies as pink daisies
    red_daisies = temp_red_daisies_multiplied - red_less_than

    # L4
    total_daisies = pink_daisies + red_daisies + white_daisies

    # FA
    answer = total_daisies
    return answer