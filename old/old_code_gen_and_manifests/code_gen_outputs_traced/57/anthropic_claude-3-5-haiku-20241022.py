def solve(
    total_butter: float = 10.0,  # Liza bought 10 kilograms of butter
    chocolate_chip_fraction: float = 1/2,  # one-half of it for chocolate chip cookies
    peanut_butter_fraction: float = 1/5,  # one-fifth of it for peanut butter cookies
    sugar_cookie_fraction: float = 1/3  # one-third of the remaining butter for sugar cookies
):
    """Index: 57.
    Returns: the amount of butter left after making three kinds of cookies.
    """

    #: L1
    chocolate_chip_butter = total_butter * chocolate_chip_fraction # eval: 5.0 = 10.0 * 0.5

    #: L2
    peanut_butter_butter = total_butter * peanut_butter_fraction # eval: 2.0 = 10.0 * 0.2

    #: L3
    butter_used_first_two = chocolate_chip_butter + peanut_butter_butter # eval: 7.0 = 5.0 + 2.0

    #: L4
    remaining_butter_after_first_two = total_butter - butter_used_first_two # eval: 3.0 = 10.0 - 7.0

    #: L5
    sugar_cookie_butter = remaining_butter_after_first_two * sugar_cookie_fraction # eval: 1.0 = 3.0 * 0.3333333333333333

    #: L6
    final_remaining_butter = remaining_butter_after_first_two - sugar_cookie_butter # eval: 2.0 = 3.0 - 1.0

    #: FA
    answer = final_remaining_butter
    return answer # eval: return 2.0
