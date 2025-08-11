def solve():
    """Index: 57.
    Returns: the kilograms of butter left after making all three kinds of cookies.
    """
    # L1
    total_butter = 10 # Liza bought 10 kilograms of butter
    chocolate_chip_divisor = 2 # one-half of it for chocolate chip cookies
    butter_for_chocolate_chip = total_butter / chocolate_chip_divisor

    # L2
    peanut_butter_divisor = 5 # one-fifth of it for peanut butter cookies
    butter_for_peanut_butter = total_butter / peanut_butter_divisor

    # L3
    butter_for_choc_and_pb = butter_for_chocolate_chip + butter_for_peanut_butter

    # L4
    butter_left_after_choc_and_pb = total_butter - butter_for_choc_and_pb

    # L5
    sugar_cookies_divisor = 3 # one-third of the remaining butter for sugar cookies
    butter_for_sugar = butter_left_after_choc_and_pb / sugar_cookies_divisor

    # L6
    butter_left_final = butter_left_after_choc_and_pb - butter_for_sugar

    # FA
    answer = butter_left_final
    return answer