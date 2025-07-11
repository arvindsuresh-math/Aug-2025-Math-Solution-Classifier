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
    butter_for_chocolate_chip = total_butter_kg / 2

    #: L2
    butter_for_peanut_butter = total_butter_kg / 5

    #: L3
    butter_used_chocolate_peanut = butter_for_chocolate_chip + butter_for_peanut_butter

    #: L4
    remaining_butter_after_two_types = total_butter_kg - butter_used_chocolate_peanut

    #: L5

    #: L6
    butter_left_final = remaining_butter_after_two_types - fraction_sugar_cookies_remaining

    #: FA
    answer = butter_left_final
    return answer