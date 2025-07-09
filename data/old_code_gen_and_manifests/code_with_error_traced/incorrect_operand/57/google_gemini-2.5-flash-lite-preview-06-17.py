def solve(
    total_butter: int = 10, # Liza bought 10 kilograms of butter
    fraction_chocolate_chip: float = 1/2, # She used one-half of it for chocolate chip cookies
    fraction_peanut_butter: float = 1/5, # one-fifth of it for peanut butter cookies
    fraction_sugar_cookies_of_remaining: float = 1/3 # one-third of the remaining butter for sugar cookies
):
    """Index: 57.
    Returns: the amount of butter in kilograms left after making three kinds of cookies.
    """

    #: L1
    butter_for_chocolate_chip = total_butter * fraction_chocolate_chip # eval: 5.0 = 10 * 0.5

    #: L2
    butter_for_peanut_butter = fraction_chocolate_chip * fraction_peanut_butter # eval: 0.1 = 0.5 * 0.2

    #: L3
    butter_used_so_far = butter_for_chocolate_chip + butter_for_peanut_butter # eval: 5.1 = 5.0 + 0.1

    #: L4
    remaining_butter_before_sugar = total_butter - butter_used_so_far # eval: 4.9 = 10 - 5.1

    #: L5
    butter_for_sugar_cookies = remaining_butter_before_sugar * fraction_sugar_cookies_of_remaining # eval: 1.6333333333333333 = 4.9 * 0.3333333333333333

    #: L6
    butter_left = remaining_butter_before_sugar - butter_for_sugar_cookies # eval: 3.266666666666667 = 4.9 - 1.6333333333333333

    #: FA
    answer = butter_left
    return answer # eval: return 3.266666666666667
