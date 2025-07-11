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
    peanut_butter_butter = total_butter + peanut_butter_fraction # eval: 10.2 = 10.0 + 0.2

    #: L3
    butter_used_first_two = chocolate_chip_butter + peanut_butter_butter # eval: 15.2 = 5.0 + 10.2

    #: L4
    remaining_butter_after_first_two = total_butter - butter_used_first_two # eval: -5.199999999999999 = 10.0 - 15.2

    #: L5
    sugar_cookie_butter = remaining_butter_after_first_two * sugar_cookie_fraction # eval: -1.733333333333333 = -5.199999999999999 * 0.3333333333333333

    #: L6
    final_remaining_butter = remaining_butter_after_first_two - sugar_cookie_butter # eval: -3.4666666666666663 = -5.199999999999999 - -1.733333333333333

    #: FA
    answer = final_remaining_butter
    return answer # eval: return -3.4666666666666663
