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
    butter_for_peanut_butter = total_butter * fraction_peanut_butter # eval: 2.0 = 10 * 0.2

    #: L3
    butter_used_so_far = butter_for_chocolate_chip + butter_for_peanut_butter # eval: 7.0 = 5.0 + 2.0

    #: L4

    #: L5
    butter_for_sugar_cookies = fraction_sugar_cookies_of_remaining * fraction_sugar_cookies_of_remaining # eval: 0.1111111111111111 = 0.3333333333333333 * 0.3333333333333333

    #: L6
    butter_left = fraction_sugar_cookies_of_remaining - butter_for_sugar_cookies # eval: 0.2222222222222222 = 0.3333333333333333 - 0.1111111111111111

    #: FA
    answer = butter_left
    return answer # eval: return 0.2222222222222222
