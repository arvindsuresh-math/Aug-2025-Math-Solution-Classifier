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
    butter_for_chocolate_chip = total_butter * fraction_chocolate_chip

    #: L2
    butter_for_peanut_butter = total_butter * fraction_peanut_butter

    #: L3
    butter_used_so_far = butter_for_chocolate_chip + butter_for_peanut_butter

    #: L4

    #: L5
    butter_for_sugar_cookies = fraction_sugar_cookies_of_remaining * fraction_sugar_cookies_of_remaining

    #: L6
    butter_left = fraction_sugar_cookies_of_remaining - butter_for_sugar_cookies

    #: FA
    answer = butter_left
    return answer