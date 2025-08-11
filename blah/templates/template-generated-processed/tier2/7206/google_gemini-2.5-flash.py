def solve():
    """Index: 7206.
    Returns: the total number of chocolates initially in the box.
    """
    # L1
    portion_nuts_decimal = 0.5 # Half have nuts
    eaten_nuts_percent_question = 80 # eat 80% of the ones with nuts
    eaten_nuts_decimal_calc = 0.8 # from solution text: 80% x .5
    eaten_nuts_portion_decimal = eaten_nuts_decimal_calc * portion_nuts_decimal
    eaten_nuts_portion_percent = 40 # from solution text: 40%

    # L2
    portion_no_nuts_decimal = 0.5 # half do not
    eaten_no_nuts_percent_question = 50 # eat half of the ones without nuts
    eaten_no_nuts_decimal_calc = 0.5 # from solution text: 50% x .5
    eaten_no_nuts_portion_decimal = eaten_no_nuts_decimal_calc * portion_no_nuts_decimal
    eaten_no_nuts_portion_percent = 25 # from solution text: 25%

    # L3
    total_eaten_percent = eaten_nuts_portion_percent + eaten_no_nuts_portion_percent

    # L4
    total_percent_whole = 100 # WK
    total_left_percent = total_percent_whole - total_eaten_percent

    # L5
    chocolates_left = 28 # 28 chocolates left
    total_left_decimal_calc = 0.35 # from solution text: .35
    initial_chocolates = chocolates_left / total_left_decimal_calc

    # FA
    answer = initial_chocolates
    return answer