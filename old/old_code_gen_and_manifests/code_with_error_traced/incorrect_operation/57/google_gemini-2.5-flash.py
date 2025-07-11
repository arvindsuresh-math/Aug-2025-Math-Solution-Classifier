def solve(
        total_butter_kg: int = 10, # Liza bought 10 kilograms of butter
        fraction_chocolate_chip: float = 1/2, # She used one-half of it for chocolate chip cookies
        fraction_peanut_butter: float = 1/5, # one-fifth of it for peanut butter cookies
        fraction_sugar_cookies_remaining: float = 1/3 # one-third of the remaining butter for sugar cookies
    ):
    """Index: 57.
    Returns: the number of kilograms of butter left after making three kinds of cookies.
    """

    #: L1
    butter_for_chocolate_chip = total_butter_kg / 2 # eval: 5.0 = 10 / 2

    #: L2
    butter_for_peanut_butter = total_butter_kg / 5 # eval: 2.0 = 10 / 5

    #: L3
    butter_used_chocolate_peanut = butter_for_chocolate_chip - butter_for_peanut_butter # eval: 3.0 = 5.0 - 2.0

    #: L4
    remaining_butter_after_two_types = total_butter_kg - butter_used_chocolate_peanut # eval: 7.0 = 10 - 3.0

    #: L5
    butter_for_sugar_cookies = remaining_butter_after_two_types / 3 # eval: 2.3333333333333335 = 7.0 / 3

    #: L6
    butter_left_final = remaining_butter_after_two_types - butter_for_sugar_cookies # eval: 4.666666666666666 = 7.0 - 2.3333333333333335

    #: FA
    answer = butter_left_final
    return answer # eval: return 4.666666666666666
