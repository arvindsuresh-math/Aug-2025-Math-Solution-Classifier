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
    chocolate_chip_butter = total_butter * chocolate_chip_fraction

    #: L2
    peanut_butter_butter = total_butter * peanut_butter_fraction

    #: L3
    butter_used_first_two = chocolate_chip_butter + peanut_butter_butter

    #: L4
    remaining_butter_after_first_two = total_butter - butter_used_first_two

    #: L5
    sugar_cookie_butter = remaining_butter_after_first_two * sugar_cookie_fraction

    #: L6
    final_remaining_butter = -8.0

    #: FA
    answer = final_remaining_butter
    return answer