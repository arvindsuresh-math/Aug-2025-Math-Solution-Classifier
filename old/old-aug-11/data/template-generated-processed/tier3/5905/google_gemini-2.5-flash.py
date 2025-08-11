def solve():
    """Index: 5905.
    Returns: the total number of dishes that include lentils.
    """
    # L1
    total_dishes = 10 # Ten dishes on their menu
    beans_lentils_dishes = 2 # Two have beans and lentils
    beans_seitan_dishes = 2 # and two have beans and seitan
    dishes_one_protein = total_dishes - beans_lentils_dishes - beans_seitan_dishes

    # L2
    half_remaining_divisor = 2 # Half of the remaining dishes
    dishes_only_beans = dishes_one_protein / half_remaining_divisor

    # L3
    seitan_ratio_divisor = 3 # three times as many dishes with only beans as with only seitan
    dishes_only_seitan = dishes_only_beans / seitan_ratio_divisor

    # L4
    dishes_only_lentils = dishes_one_protein - dishes_only_beans - dishes_only_seitan

    # L5
    total_dishes_with_lentils = dishes_only_lentils + beans_lentils_dishes

    # FA
    answer = total_dishes_with_lentils
    return answer