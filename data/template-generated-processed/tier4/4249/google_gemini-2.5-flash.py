def solve():
    """Index: 4249.
    Returns: the total number of marbles Courtney has.
    """
    # L1
    first_jar_marbles = 80 # One jar had 80 marbles
    second_jar_multiplier = 2 # twice that amount
    second_jar_marbles = second_jar_multiplier * first_jar_marbles

    # L2
    third_jar_fraction_decimal = 0.25 # 1/4 the amount of her first jar (used as .25)
    third_jar_fraction_num_calc = 1 # 1/4 the amount of her first jar (for calculator)
    third_jar_fraction_den_calc = 4 # 1/4 the amount of her first jar (for calculator)
    third_jar_marbles = third_jar_fraction_decimal * first_jar_marbles

    # L3
    total_marbles = first_jar_marbles + second_jar_marbles + third_jar_marbles

    # FA
    answer = total_marbles
    return answer