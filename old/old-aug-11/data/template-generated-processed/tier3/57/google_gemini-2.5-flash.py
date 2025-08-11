def solve():
    """Index: 57.
    Returns: the amount of butter left after making three kinds of cookies.
    """
    # L1
    total_butter = 10 # 10 kilograms of butter
    chocolate_chip_divisor = 2 # one-half of it
    butter_for_chocolate_chip = total_butter / chocolate_chip_divisor

    # L2
    peanut_butter_divisor = 5 # one-fifth of it
    butter_for_peanut_butter = total_butter / peanut_butter_divisor

    # L3
    butter_used_chocolate_peanut = butter_for_chocolate_chip + butter_for_peanut_butter

    # L4
    remaining_butter_after_two_types = total_butter - butter_used_chocolate_peanut

    # L5
    sugar_cookie_divisor = 3 # one-third of the remaining butter
    butter_for_sugar_cookies = remaining_butter_after_two_types / sugar_cookie_divisor

    # L6
    final_remaining_butter = remaining_butter_after_two_types - butter_for_sugar_cookies

    # FA
    answer = final_remaining_butter
    return answer